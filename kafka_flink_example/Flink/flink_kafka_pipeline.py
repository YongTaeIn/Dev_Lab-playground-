import os
from pathlib import Path
from pyflink.common import Types, WatermarkStrategy
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import (
    KafkaSource,
    KafkaOffsetsInitializer,
    KafkaSink,
    KafkaRecordSerializationSchema,
)


def main() -> None:
    ### 엔트리 포인트 설정 ###
    topic = os.getenv("KAFKA_TOPIC", "raw-topic")
    bootstrap = os.getenv("KAFKA_BOOTSTRAP", "localhost:19092")
    group_id = os.getenv("KAFKA_GROUP_ID", "flink-print-group")
    sink_topic = os.getenv("KAFKA_SINK_TOPIC", "processed-topic")

    ### 스트림 실행 환경 설정 ###
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(int(os.getenv("FLINK_PARALLELISM", "1")))
    
    # Kafka 커넥터 JAR 파일 설정 (기본적으로 Flink는 kafka 를 바로 읽고 쓸 수없음. 커넥터 모듈이 필요함.)
    # jar파일은 드라이버/플러그인 같은 느낌임.
    jar_path = Path(__file__).parent / "flink-sql-connector-kafka-3.1.0-1.18.jar"
    jar_uri = jar_path.absolute().as_uri()  # 공백이 포함된 경로를 올바르게 URL 인코딩
    env.add_jars(jar_uri)

    ### Kafka source 설정 ###
    source = (
        KafkaSource.builder()
        .set_bootstrap_servers(bootstrap) # 브로커 지정
        .set_topics(topic) # 토픽 지정
        .set_group_id(group_id) # 그룹 아이디 지정
        .set_starting_offsets(KafkaOffsetsInitializer.earliest()) # 처음부터 읽기
        .set_value_only_deserializer(SimpleStringSchema()) # 문자열로 역직렬화
        .build()
    )

    ### Kafka source 데이터 읽기 ###
    ds = env.from_source(source, watermark_strategy=WatermarkStrategy.no_watermarks(), source_name="kafka-source", type_info=Types.STRING())

    # Identity transformation (pass-through). You can map/transform here if needed.
    ### 데이터 변환 ###
    transformed = ds.map(lambda x: f"Processed: {x}", output_type=Types.STRING())

    # Print to terminal (stdout)
    ### 데이터 출력 ###
    transformed.print()

    ### Kafka sink 설정 ###
    '''
        kafka sink는 Flink에서 지원하는 kafka 커넥터 모듈임.
        - Kafka topic에 저장된 데이터를 외부 시스템으로 내보내는 역할을 하는 구성 요소, 혹은 동작 방식을 의미함.
    '''
    sink = (
        KafkaSink.builder()
        .set_bootstrap_servers(bootstrap) # 브로커 지정
        .set_record_serializer(
            KafkaRecordSerializationSchema.builder()
            .set_topic(sink_topic) # 토픽 지정
            .set_value_serialization_schema(SimpleStringSchema()) # 문자열을 바이트로 간단히 직렬화
            .build()
        )
        .build()
    )
    # 즉, 변환된 데이터를 Kafka sink topic에 쓰기

    transformed.sink_to(sink) 

    env.execute("print-from-kafka")


if __name__ == "__main__":
    main()



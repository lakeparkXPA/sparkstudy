# Spark 3.5.5 tutorial
Apache Spark 공식 문서 스터디


### Quick Start
2025.04.14
윈도우 환경에서 맥 환경으로 변경<br>
첫 시작 simpleApp.py 돌리니 <br>
Can't assign requested address: Service 'sparkDriver' failed after 16 retries (on a random free port)! Consider explicitly setting the appropriate binding address for the service 'sparkDriver' (for example spark.driver.bindAddress for SparkDriver) to the correct binding address.
<br> 에러 발생 <br>-> spark session 객체에서 config 설정에 127.0.0.1 추가 
<br> 혹은 load-spark-env.sh 설정에서 주소 설정

<br>
2025.04.10<br>
시작
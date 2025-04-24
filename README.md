# Spark 3.5.5 tutorial
Apache Spark 공식 문서 스터디

## RDD Programming Guide
2025.04.24  
복습 및 실습 진행  
Printing elements of an RDD  


2025.04.23  
복습 및 실습 진행  
Understanding closures  

2025.04.22  
복습 및 실습 진행  
Passing Functions to Spark  

2025.04.20  
복습 및 실습 진행  
RDD Operation  

2025.04.17  
복습 및 실습 진행
  
2025.04.16  
실습 진행  

2025.04.15  
코드 실습은 jupyternotebook 이 편리해보여서 변경  
### Spark abstraction
Spark 앱은 사용자의 main function을 클러스터에서 병렬처리하는 driver program 으로 구성됨  
#### Resilient Distributed Dataset(RDD)
하둡 내에 있는 파일 혹은 디스크에 저장된 Scala collection 으로 시작해서 이를 RDD로 변환한다.
RDD 는 메모리 위에 두어서 병렬처리에서 효율적으로 재사용  
RDD 는 node의 실패에서 자동으로 회복
#### Shared variables
spark는 function 서로 다른 nodes 에서 작업 묶음으로 병렬 작동  
function 의 변수를 복사해서 각 노드에 전달  
- Broadcast variable  
한 값을 모든 node 의 메모리에 cache  
- Accumulatiors  
누적용 변수, sum or count 연산에 쓰임, 각 작업에서 값을 더해 나가면서 그 결과를 드라이버 프로그램에서 수집, += 처럼 누적 가능, 읽는건 드라이버 프로그램에서만 가능

## Quick Start
2025.04.14  
윈도우 환경에서 맥 환경으로 변경  
첫 시작 simpleApp.py 돌리니  
Can't assign requested address: Service 'sparkDriver' failed after 16 retries (on a random free port)! Consider explicitly setting the appropriate binding address for the service 'sparkDriver' (for example spark.driver.bindAddress for SparkDriver) to the correct binding address.  
에러 발생   
-> spark session 객체에서 config 설정에 127.0.0.1 추가  
혹은 load-spark-env.sh 설정에서 주소 설정

2025.04.10  
시작
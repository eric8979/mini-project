# 🚌 Bus Passenger Data

Bus Passenger Data by "Bus Route", "Bus Stop" and "Time". (By Month)

* Only of Seoul +around area included.

## Folder Description

* zipData/ : Raw bus stats data to show what data was used in this project. Don't need to download this dir.

* trimmedData/ : Trimmed zipData.

## Data Origin

[Seoul Bus Data Link](http://data.seoul.go.kr/dataList/OA-12913/S/1/datasetView.do)

## Dev Log

* Found wrong formatting. Some comma were wrongly used.

e.g) "750번(A,신촌,수색교~서울대)"

The example above supposed to be single datum piece.

* Found not all file is formatted the same. 

Some files have double quotes and some aren't.

## Raw info

서울시 버스노선별 정류장별 시간대별 승하차 인원 정보
교통카드(선후불교통카드 및 1회용 교통카드)를 이용한 버스노선별 정류장별 시간대별 승하차인원을 나타내는 정보입니다. (월단위) 서울버스 대상 (서울시내, 서울광역, 서울마을)

(* 데이터 적재는 매월 5일 전월 데이터를 갱신합니다.)
* 2022년 06월이후 데이터부터 '교통수단타입명','교통수단타입코드'가 추가되었습니다.

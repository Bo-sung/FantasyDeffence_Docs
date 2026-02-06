# Enum 정의

[← README](README.md)

---

## Rotation (건물 방향)

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | NORTH | 북쪽 (위) |
| 90 | EAST | 동쪽 (오른쪽) |
| 180 | SOUTH | 남쪽 (아래) |
| 270 | WEST | 서쪽 (왼쪽) |

```typescript
enum Rotation {
  NORTH = 0,
  EAST = 90,
  SOUTH = 180,
  WEST = 270
}
```

---

## BuildingCategory (건물 분류)

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | PRODUCTION | 생산 시설 (농장, 마력 정제소 등) |
| 1 | HOUSING | 주거 시설 (민가, 연립 주택 등) |
| 2 | COMFORT | 편의 시설 (우물, 방앗간 등) |
| 3 | MILITARY | 군사 시설 (무기고, 공병 작업장 등) |
| 4 | FUNCTION | 기능 시설 (주점, 대장간 등) |
| 5 | DECORATION | 장식 시설 (도로, 가로등 등) |

```typescript
enum BuildingCategory {
  PRODUCTION = 0,
  HOUSING = 1,
  COMFORT = 2,
  MILITARY = 3,
  FUNCTION = 4,
  DECORATION = 5
}
```

---

## BuildingState (건물 상태)

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | BUILDING | 건설 중 |
| 1 | ACTIVE | 활성 (정상 작동) |
| 2 | INACTIVE | 비활성 (작동 중지) |
| 3 | DESTROYED | 파괴됨 |

```typescript
enum BuildingState {
  BUILDING = 0,
  ACTIVE = 1,
  INACTIVE = 2,
  DESTROYED = 3
}
```

---

## ResourceType (자원 종류)

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | SILVER | 은화 |
| 1 | FOOD | 식량 |
| 2 | MANA | 마석 |
| 3 | SUPPLY | 보급 |
| 4 | MANPOWER | 인력 |

```typescript
enum ResourceType {
  SILVER = 0,
  FOOD = 1,
  MANA = 2,
  SUPPLY = 3,
  MANPOWER = 4
}
```

---

## ZoneType (구역 종류)

| 값 | 이름 | 설명 |
|----|------|------|
| 0 | START | 시작 영역 |
| 1 | PLAINS | 평원 |
| 2 | RIVERSIDE | 강변 |
| 3 | FOREST | 숲 |
| 4 | SWAMP | 습지 |
| 5 | MOUNTAIN | 산악 |
| 6 | COAST | 해안 |

```typescript
enum ZoneType {
  START = 0,
  PLAINS = 1,
  RIVERSIDE = 2,
  FOREST = 3,
  SWAMP = 4,
  MOUNTAIN = 5,
  COAST = 6
}
```

---

## ErrorCode (에러 코드)

| 값 | 이름 | 설명 |
|----|------|------|
| E001 | OUT_OF_BOUNDS | 좌표 범위 초과 |
| E002 | COLLISION | 건물 충돌 |
| E003 | FIXED_AREA | 고정 영역 침범 |
| E004 | NOT_UNLOCKED | 해금 조건 미충족 |
| E005 | MAX_COUNT | 최대 개수 초과 |
| E006 | INVALID_ROTATION | 잘못된 회전 값 |
| E007 | INSUFFICIENT_RESOURCE | 자원 부족 |

```typescript
enum ErrorCode {
  OUT_OF_BOUNDS = "E001",
  COLLISION = "E002",
  FIXED_AREA = "E003",
  NOT_UNLOCKED = "E004",
  MAX_COUNT = "E005",
  INVALID_ROTATION = "E006",
  INSUFFICIENT_RESOURCE = "E007"
}
```

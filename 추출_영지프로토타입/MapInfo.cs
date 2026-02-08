using System;
using System.Collections.Generic;

namespace Estate
{
    #region Enums

    /// <summary>
    /// 건물 방향
    /// </summary>
    public enum Rotation
    {
        North = 0,
        East = 90,
        South = 180,
        West = 270
    }

    /// <summary>
    /// 건물 분류
    /// </summary>
    public enum BuildingCategory
    {
        Production = 0,   // 생산 시설
        Housing = 1,      // 주거 시설
        Comfort = 2,      // 편의 시설
        Military = 3,     // 군사 시설
        Function = 4,     // 기능 시설
        Decoration = 5    // 장식 시설
    }

    /// <summary>
    /// 건물 상태
    /// </summary>
    public enum BuildingState
    {
        Building = 0,     // 건설 중
        Active = 1,       // 활성
        Inactive = 2,     // 비활성
        Destroyed = 3     // 파괴됨
    }

    #endregion

    #region Data Classes

    /// <summary>
    /// 2D 좌표
    /// </summary>
    [Serializable]
    public class Position
    {
        public int x;
        public int y;

        public Position() { }

        public Position(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }

    /// <summary>
    /// 배치 가능한 오브젝트 (공통 베이스)
    /// </summary>
    [Serializable]
    public class Placeable
    {
        public string id;           // 인스턴스 고유 ID
        public int typeId;          // 타입 ID (config 참조)
        public Position position;   // 배치 좌표
        public Rotation rotation;   // 방향

        public Placeable()
        {
            position = new Position();
        }
    }

    /// <summary>
    /// 건물 배치 정보
    /// </summary>
    [Serializable]
    public class Building : Placeable { }

    /// <summary>
    /// 지형 배치 정보 (도로, 장식 바닥 등)
    /// </summary>
    [Serializable]
    public class Terrain : Placeable { }

    /// <summary>
    /// 맵 데이터 (배치 정보)
    /// </summary>
    [Serializable]
    public class MapData
    {
        public List<Building> buildings;
        public List<Terrain> terrain;

        public MapData()
        {
            buildings = new List<Building>();
            terrain = new List<Terrain>();
        }
    }

    /// <summary>
    /// 맵 정보 (메타데이터 + 맵 데이터)
    /// </summary>
    [Serializable]
    public class MapInfo
    {
        public string user;          // 유저 ID
        public string description;   // 설명
        public string version;       // 버전
        public DateTime date;        // 생성/수정 일시
        public MapData mapData;      // 실제 맵 데이터

        public MapInfo()
        {
            mapData = new MapData();
        }
    }

    /// <summary>
    /// JSON 루트 (직렬화용)
    /// </summary>
    [Serializable]
    public class MapInfoRoot
    {
        public MapInfo mapinfo;

        public MapInfoRoot()
        {
            mapinfo = new MapInfo();
        }
    }

    #endregion
}

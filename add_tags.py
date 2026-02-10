#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YAML Front Matter 태그 추가 스크립트
모든 마크다운 문서에 tags: [plan, client, server] 추가
"""

import os
import re
from pathlib import Path

# 문서별 태그 매핑
TAG_MAPPING = {
    # ============================================================
    # tags: [plan] - 기획 전용
    # ============================================================
    "프로젝트 목표.md": ["plan"],
    "세계관 기획서.md": ["plan"],
    "아트 방향성 기획서.md": ["plan"],

    # 세계관 하위 문서
    "세계관/NPC 설정.md": ["plan"],
    "세계관/대륙·지리 구조.md": ["plan"],
    "세계관/세계관 개요.md": ["plan"],
    "세계관/세력 구조.md": ["plan"],
    "세계관/스토리 구조.md": ["plan"],
    "세계관/역사 연표.md": ["plan"],
    "세계관/주인공 설정.md": ["plan"],
    "세계관/플레이어용 세계관 소개.md": ["plan"],

    # 시스템 기획
    "시스템/게임 모드.md": ["plan"],
    "시스템/진행 시스템.md": ["plan"],
    "시스템/소셜 시스템.md": ["plan"],
    "시스템/수익화 모델.md": ["plan"],
    "시스템/KPI 지표.md": ["plan"],
    "시스템/개발 로드맵.md": ["plan"],

    # ============================================================
    # tags: [plan, client] - 기획 + 클라이언트
    # ============================================================
    "시스템/게임 개요.md": ["plan", "client"],
    "시스템/스탯 시스템.md": ["plan", "client"],
    "시스템/스테이지 시스템.md": ["plan", "client"],
    "시스템/전투 메카닉.md": ["plan", "client"],
    "시스템/스킬 시스템.md": ["plan", "client"],
    "시스템/적 시스템.md": ["plan", "client"],
    "시스템/영웅 시스템.md": ["plan", "client"],
    "시스템/장비 시스템.md": ["plan", "client"],
    "시스템/재화 시스템.md": ["plan", "client"],
    "시스템/재화 시스템_상세.md": ["plan", "client"],
    "시스템/UI 설계.md": ["plan", "client"],
    "시스템/기술 요구사항.md": ["plan", "client"],

    # ============================================================
    # tags: [plan, client, server] - 영웅 시스템 (서버 검증 필요)
    # ============================================================
    "시스템/영웅/육성 시스템.md": ["plan", "client", "server"],
    "시스템/영웅/획득 시스템.md": ["plan", "client", "server"],
    "시스템/영웅/링크 시스템.md": ["plan", "client", "server"],
    "시스템/영웅/수리 시스템.md": ["plan", "client", "server"],

    # ============================================================
    # tags: [plan, server] - 기획 + 서버
    # ============================================================
    "시스템/영지/생산 시스템.md": ["plan", "server"],
    "시스템/영지/세금 시스템.md": ["plan", "server"],
    "시스템/영지/만족도 시스템.md": ["plan", "server"],

    # ============================================================
    # tags: [plan, client, server] - 공통
    # ============================================================
    "용어 사전.md": ["plan", "client", "server"],
    "시스템/데이터 테이블.md": ["plan", "client", "server"],
    "시스템/영지 시스템.md": ["plan", "client", "server"],
    "시스템/영지/맵·구역 시스템.md": ["plan", "client", "server"],
    "시스템/영지/건설 시스템.md": ["plan", "client", "server"],
    "시스템/영지/건물 목록.md": ["plan", "client", "server"],
    "시스템/영지/영웅 배치.md": ["plan", "client", "server"],
    "시스템/영지/데이터 명세.md": ["plan", "client", "server"],

    # ============================================================
    # tags: [server] - 서버 전용
    # ============================================================
    "시스템/서버 아키텍처.md": ["server"],
    "시스템/데이터 아키텍처.md": ["server"],
}


def has_yaml_frontmatter(content: str) -> bool:
    """파일이 이미 YAML Front Matter를 가지고 있는지 확인"""
    return content.strip().startswith("---")


def add_yaml_frontmatter(content: str, tags: list) -> str:
    """YAML Front Matter 추가"""
    tags_str = ", ".join(tags)
    frontmatter = f"---\ntags: [{tags_str}]\n---\n\n"
    return frontmatter + content


def process_file(file_path: Path, tags: list):
    """파일에 YAML Front Matter 추가"""
    try:
        # UTF-8 BOM 처리 포함
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()

        # 이미 YAML Front Matter가 있으면 스킵
        if has_yaml_frontmatter(content):
            print(f"[SKIP] (already tagged): {file_path.relative_to(Path.cwd())}")
            return

        # YAML Front Matter 추가
        new_content = add_yaml_frontmatter(content, tags)

        # 파일 저장
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"[OK] [{', '.join(tags)}]: {file_path.relative_to(Path.cwd())}")

    except Exception as e:
        print(f"[ERROR]: {file_path.relative_to(Path.cwd())} - {e}")


def main():
    """메인 실행 함수"""
    base_path = Path(__file__).parent
    processed = 0
    skipped = 0
    errors = 0

    print("=" * 60)
    print("YAML Front Matter 태그 추가 시작")
    print("=" * 60)

    for relative_path, tags in TAG_MAPPING.items():
        file_path = base_path / relative_path

        if not file_path.exists():
            print(f"[WARNING] File not found: {relative_path}")
            errors += 1
            continue

        if has_yaml_frontmatter(file_path.read_text(encoding='utf-8-sig')):
            skipped += 1
        else:
            process_file(file_path, tags)
            processed += 1

    print("\n" + "=" * 60)
    print(f"Complete: {processed} added | Skipped: {skipped} | Errors: {errors}")
    print("=" * 60)


if __name__ == "__main__":
    main()

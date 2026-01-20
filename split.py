import re
from pathlib import Path

def split_to_sentences(filename: str):
    """
    같은 폴더에 있는 filename을 읽어서
    filename_sentences.txt 로 문장별 저장
    """
    in_path = Path(filename).expanduser().resolve()
    text = in_path.read_text(encoding="utf-8")

    # 문장 끝 (. ? !) 뒤의 공백 기준으로 분리
    parts = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in parts if s.strip()]

    out_path = in_path.with_name(in_path.stem + "_sentences.txt")
    out_path.write_text("\n".join(sentences), encoding="utf-8")

    print(f"저장 완료: {out_path}")

# 사용 예시
split_to_sentences("output/subtitles/result.txt")   # 같은 폴더에 있는 mytext.txt 처리

import os
import argparse
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


def download_file(url: str, output_dir: str):
    local_filename = url.split("/")[-1]
    local_filepath = os.path.join(output_dir, local_filename)

    response = requests.get(url, stream=True)
    total = int(response.headers.get("content-length", 0))

    # if requested url is not file, return None
    if total == 0:
        print("요청하신 URL은 파일이 아닙니다.")
        return None

    # if file already exists, ask user to overwrite
    if os.path.exists(local_filepath):
        print(f"파일이 이미 존재합니다: {local_filepath}")
        answer = input("덮어쓰시겠습니까? (y/n): ")
        if answer.lower() != "y":
            return None
        else:
            with open(local_filepath, "wb") as f, tqdm(
                total=total,
                unit="iB",
                unit_scale=True,
                unit_divisor=1024,
                bar_format="{l_bar}{bar:10}{r_bar}",
            ) as bar:
                for data in response.iter_content(chunk_size=1024):
                    f.write(data)
                    bar.update(len(data))
            return local_filepath


def main():
    parser = argparse.ArgumentParser(description="파일 다운로드")
    parser.add_argument("url", help="다운로드할 파일의 URL")
    parser.add_argument("-o", "--output", default=".", help="다운로드할 디렉터리")
    parser.add_argument(
        "-t", "--threads", type=int, default=1, help="다운로드에 사용할 스레드 수"
    )
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    try:
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            future = executor.submit(download_file, args.url, args.output)
            result = future.result()
            if result:
                print(f"다운로드가 완료되었습니다: {result}")

    except Exception as e:
        print(f"다운로드 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()

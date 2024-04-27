import azure.functions as func


def main(blob: func.InputStream):
    # blob 처리 로직
    print(
        f"Processing blob\n"
        f"Name: {blob.name}\n"
        f"Blob Size: {len(blob.read())} bytes"
    )

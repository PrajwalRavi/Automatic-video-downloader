import os


class GetInput:
    path = input().strip()
    files = os.listdir(path)

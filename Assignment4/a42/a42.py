from art_config import ArtConfig
from color import Color

def main() -> None:
    art_config = ArtConfig(Color(-1, -1, -1, -1))
    for i in range(1, 11):
        art_config.gen_shape()
    art_config.print_table()

if __name__ == "__main__":
    main()
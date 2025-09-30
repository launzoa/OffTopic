import PIL.Image

CARACTERES_ASCII = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]


# Recebe um objeto de imagem e uma nova largura, e retorna a imagem redimensionada
def resizeImage(image, new_width):
    width, heigth = image.size
    proportion = heigth / width
    new_heigth = int(new_width * proportion * 0.55)
    image_resized = image.resize((new_width, int(new_heigth)))

    return image_resized


# Converte uma imagem em escala de cinza
def convertToGrayScale(image):
    return image.convert("L")


# Converte a imagem para uma string de arte ASCII.
def mappingPixelsToAscii(image, chars):
    img_gray = convertToGrayScale(image)
    pixels = img_gray.getdata()

    pixels_mapping = [chars[int(pixel / 255 * (len(chars) - 1))] for pixel in pixels]
    string = "".join(pixels_mapping)

    width = image.width
    art = ""
    for i in range(0, len(string), width):
        art += string[i : i + width] + "\n"

    return art


# Salva a string de arte ASCII final em um arquivo de texto.
def saveArt(art, path="ascii_image.txt"):
    with open(path, "w") as f:
        f.write(art)
    print(f"Conversão feita com sucesso e salva no arquivo '{path}'")


# Faz a chamada das funções anteriores em uma função "principal"
def main():
    path = input("Digite o caminho para a imagem: \n")

    try:
        image = PIL.Image.open(path)
    except FileNotFoundError:
        print(
            f"Erro: O arquivo '{path}' não foi encontrado."
            + "Verifique o caminho e tente novamente."
        )
        return

    image_resized = resizeImage(image, new_width=180)
    ascii_art = mappingPixelsToAscii(image_resized, CARACTERES_ASCII)
    saveArt(ascii_art)


# Main
if __name__ == "__main__":
    main()

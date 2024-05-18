from PIL import Image
from Cuif import Cuif
import math


def PSNR(original,decodificada,b):
    try:
        mse = MSE(original,decodificada) 
        psnr = 10*math.log10(((2**b-1)**2)/mse)
        return psnr
    except ZeroDivisionError:
        return "Infinito"


def MSE(ori, dec):
    nsymbols = ori.width * ori.height * 3
    r, g, b = (0, 0, 0)
    for i in range(ori.width):
        for j in range(ori.height):
            ori_r, ori_g, ori_b = ori.getpixel((i, j))
            dec_r, dec_g, dec_b = dec.getpixel((i, j))

            r += (ori_r-dec_r)**2
            g += (ori_g-dec_g)**2
            b += (ori_b-dec_b)**2

    return (r+g+b)/nsymbols


if __name__ == "__main__":
    # filepath = '/content/drive/MyDrive/PraticaIII/mandril.bmp'
    filepath = 'mandril.bmp'
    img = Image.open(filepath)
    matriculas = [20100516, 20103689, 20104135]
    
    # instancia objeto Cuif, convertendo imagem em CUIF.1
    #cuif = Cuif(img,1,matriculas)
    cuif = Cuif(img,2,matriculas)
    
    # imprime cabeçalho Cuif
    cuif.printHeader()
    
    # mostra imagem Cuif
    cuif.show()
    
    #gera o arquivo Cuif.X
    #cuif.save('mandril1.cuif')
    cuif.save('mandril2.cuif')

    #Abre um arquivo Cuif e gera o objeto Cuif
    #cuif1 = Cuif.openCUIF('mandril1.cuif')
    cuif2 = Cuif.openCUIF('mandril2.cuif')
    
    # Converte arquivo Cuif em BMP e mostra
    #cuif1.saveBMP("mandril1.bmp")
    #cuif1.show()
    cuif2.saveBMP("mandril2.bmp")
    cuif2.show()
    
    #img1 = Image.open("mandril1.bmp")
    img2 = Image.open("mandril2.bmp")

    #psnr = PSNR(img, img1, 8)
    psnr = PSNR(img, img2, 8)
    print(f'Cálculo do PSNR: {psnr}')
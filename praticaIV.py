''' 
INE5431 Sistemas Multim��dia
Prof. Roberto Willrich

Aula Pr�tica IV: Compress�o de Entropia

'''

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
    
    # Leitura da imagem 
    filepath = 'mandril.bmp'

    img = Image.open(filepath)
    
    # Indique a matr��cula dos alunos do grupo na lista abaixo
    matriculas = [20100516, 20103689, 20104135]
    
    
    # Gera��o do arquivo Cuif.1, converte o arquivo Cuif.1 em BMP, e calcula o PSNR
    cuif1 = Cuif(img,4,matriculas)
    cuif1.printHeader()
    cuif1.show()
    cuif1.save('mandril4.cuif')
    cuif1.saveBMP('mandril4.bmp')
    img1 = Image.open('mandril4.bmp')
    print("PSNR do CUIF.4",PSNR(img,img1,8)) 
    

    print("THE END")

import os, pygame
from loguru import logger


font_registry_dict = {

}

image_registry_dict = {

}

def load_fonts(_font_dir):
    
    #this function allows programmers to automatically load fonts by
    #putting them in a directory and calling a function.
    #this makes your code cleaner when handling a sizable amount of fonts.

    try:
        _file_list = os.listdir(_font_dir)
        logger.info(str(len(_file_list))+ ' fonts found.')
        processnumber = 0
        for i in range(len(_file_list)):
            global font_registry_dict
            try:
                font_registry_dict[os.listdir(_font_dir)[processnumber]] = pygame.font.Font(_font_dir+(os.listdir(_font_dir)[processnumber], 32)) 
            except Exception as e:
                logger.error(e)
    except Exception as e:
        logger.error(e)

def load_images(_img_dir):
    
    #this function allows programmers to automatically load images by
    #simply putting them in a directory and calling a function. 
    #This makes your code cleaner when handling a large amount of images
    



    _file_list = os.listdir(_img_dir)
    logger.info(str(len(_file_list))+' images found.')
    processnumber = 0
    for i in range(len(_file_list)):
        global image_registry_dict

                    

            

        
        image_registry_dict[os.listdir(_img_dir)[processnumber]] = pygame.image.load(_img_dir+(os.listdir(_img_dir)[processnumber]))
        
        logger.info('Loaded' + os.listdir(_img_dir)[processnumber])
            

        processnumber += 1
    logger.info(image_registry_dict)
    print(image_registry_dict)
    logger.info(str(len(_file_list))+ ' images have been loaded.')

    

        

if __name__ == '__main__':
    print(os.path.basename(os.listdir('/Users/mohammedyussuf/Projects/engineruntest/images')[0]))


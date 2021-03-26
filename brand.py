from PIL import Image
import os, sys
class brand():
    def __init__(self, img_name, logo_name, logo_size=100, position = 'LT', margin=0, watermark=False):
        self.img_name = img_name
        self.position = position
        self.suffix = 'logo'

        if logo_size != 0:
            self.logo_size = logo_size/100 #logo size in percent 
        else:
            print('I think, the logo is too small')

        try: # get photo and logo 
            with Image.open(img_name) as photo_org:
                self.photo = photo_org.copy()
            with Image.open(logo_name) as logo_org:
                self.logo = logo_org.copy()
        except IOError:
            print('No such file')
        else:
            self.photo_w, self.photo_h = self.photo.size
            
            self.logo_w, self.logo_h = [int((x * self.logo_size)) for x in self.logo.size]
            self.logo.thumbnail((self.logo_w, self.logo_h), Image.ANTIALIAS)
            
            if margin: #add margin to logo
                self.logo=self.add_margin(self.logo, margin)
                
            if watermark == True:
                self.logo = self.watermark(self.photo, self.logo)
                self.suffix = 'watermark'
            self.merge()

    def merge(self): #merge photo and logo
        self.logo_w, self.logo_h = self.logo.size 
        self.photo.paste(self.logo, self.logo_position(self.position), self.logo)
        self.photo.save(f'{self.img_name.split(".")[0]}_{self.suffix}.jpg', 'JPEG')
    

    def logo_position(self, position):
        ''' Method return a logo position (x,y) based on position parameters  
            LT  CT  RT  |   Left Top        Center Top      Right Top
            LC  CC  RC  |   Left Center     Center Center   Right Center
            LB  CB  RB  |   Left Bottom     Center Bottom   Right Bottom
        '''
        position=position.upper()
        if position == 'LT':
            return (0, 0)
        elif position == 'CT':
            return (self.photo_w//2 - self.logo_w//2, 0)
        elif position == 'RT':
            return (self.photo_w - self.logo_w, 0)
        elif position == 'LC' :
            return (0, self.photo_h//2 - self.logo_h//2)
        elif position == 'CC':
            return (self.photo_w//2 - self.logo_w//2, self.photo_h//2 - self.logo_h//2)
        elif position == 'RC':
            return (self.photo_w - self.logo_w, self.photo_h//2 - self.logo_h//2)
        elif position == 'LB':
            return (0, self.photo_h - self.logo_h)
        elif position == 'CB':
            return (self.photo_w//2 - self.logo_w//2, self.photo_h - self.logo_h)
        elif position == 'RB':
            return (self.photo_w - self.logo_w, self.photo_h - self.logo_h)
        else:
            raise ValueError('Unknown parameter')


    def add_margin(self, image, margin):
        margin=abs(margin)
        image_w, image_h = image.size
        new_image = Image.new(image.mode, (image_h+margin*2, image_h+margin*2), color=(255, 255, 255, 0))
        new_image.paste(image, (margin, margin))
        return new_image

    def watermark(self, image, logo):
        new_image = Image.new(logo.mode, image.size, color=(0, 0, 0, 0))
        mask = logo.copy()
        logo.putalpha(30)

        for x in range(0, image.size[0], logo.size[0]):
            for y in range(0, image.size[1], logo.size[1]):
                new_image.paste(logo, (x,y), mask) 
        return new_image

if __name__ == '__main__':
    if len(sys.argv) == 3:
        img, logo = sys.argv[1:]
        brand(img, logo)
    
    elif len(sys.argv) == 4:
        img, logo, logo_size = sys.argv[1:]
        try:
            brand(img, logo, int(logo_size))
        except ValueError:
            print('ERROR: Wrong type of argument')
    
    elif len(sys.argv) == 5:
        img, logo, logo_size, position = sys.argv[1:]
        try:
            if position == 'W':
                brand(img, logo, int(logo_size), watermark=True)
            else:
                brand(img, logo, int(logo_size), position)
        except ValueError:
            print('ERROR: Wrong type of argument\n')
    
    elif len(sys.argv) == 6:
        img, logo, logo_size, position, margin = sys.argv[1:]
        try:
            brand(img, logo, int(logo_size), position, int(margin))
        except ValueError:
            print('ERROR: Wrong type of argument\n')
    else:
        print('Error: Enter any necessary arguments\n \tphoto_path logo_path *logo_size *position or W *margin\n\t\t*optional arguments')
from django.test import TestCase
# Create your tests here.
from .models import Profile,Comments,Image
from django.contrib.auth.models import User
import datetime as dt


class ProfileTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.user = User.objects.create(id =1,username='riri')
        self.profile = Profile(firstname = ' Rita',lastname = 'umutoni,profile_photo = 'babyb.jpeg',bio = 'Nice',date = '12.2.2121', user = self.user)
  

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.profile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=1) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.profile.save_profile()
        profile=Profile.delete_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=0) 

        

class CommentTestClass(TestCase):

    def setUp(self):
     
        self.comment=Comments.objects.create(comment='goood')
      

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.comment.save_comments()
        comment=Comments.objects.all()
        self.assertTrue(len(comm)>0) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.comment.save_comments()
        self.comment.delete_comments()
        comment=Comments.objects.all()
        self.assertTrue(len(comm)>0)
       



class ImageTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.image = Image(image ='babyb.jpeg', image_name='test', image_caption='this is a test image',date='12.9.2019')

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()

        # Testing Instance
        def test_instance(self):
            self.assertTrue(isinstance(self.image,Image))

        # Testing the save method
        def test_save_method(self):
            self.image=Image(name='cat',description='beautiful',user=self.user1,likes="1",post="image")
            self.image.save_image()
            images = Image.objects.all()
            self.assertTrue(len(images) >= 1)

    

    def test_delete_method(self):
            self.image=Image(name='cat',description='beautiful',user=self.user1,likes="1",post="image")
            self.image.save_image()
            images = self.image.delete_image
            deleted = Image.objects.all()
            self.assertTrue(len(deleted) <= 0)

        

  


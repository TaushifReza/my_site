from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


# The Tag class represents a tag with a caption attribute.
class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption


# The below class defines an Author model with fields for first name, last name, and email address.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# The above class defines a model for a blog post with various fields such as title, excerpt, image
# name, date, slug, content, author, and tags.
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        """
        The above function returns the title of an object as a string.
        :return: The `__str__` method is returning the `title` attribute of the object.
        """
        return self.title


# The Comment class represents a comment made by a user on a Post object, and it includes fields for
# the user's name, email, the comment text, and a foreign key relationship to the Post object.
class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")

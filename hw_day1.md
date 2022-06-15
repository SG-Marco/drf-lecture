### Sample code to use args, kwargs

```python
def arg_kwarg_sample(*args, **kwargs):
    print(sum(args))
    print(kwargs.keys(), kwargs.values(), kwargs.items())
    for kwarg in kwargs.items():
        print(kwarg[0], ":",kwarg[1])
    pass


nums = [5, 1, 100, 49]
profile = {
    'name': 'John',
    'address': 'Seoul',
    'phone': '010-0000-0000'
}

arg_kwarg_sample(*nums, **profile)

```


### Mutable VS Immutable


#### Mutable Definition
Mutable is when something is changeable or has the ability to change. In Python, ‘mutable’ is the ability of objects to change their values. These are often the objects that store a collection of data.

#### Immutable Definition
Immutable is the when no change is possible over time. In Python, if the value of an object cannot be changed over time, then it is known as immutable. Once created, the value of these objects is permanent.

##### List of Mutable and Immutable objects

1. Objects of built-in type that are mutable are:

- Lists
- Sets
- Dictionaries
- User-Defined Classes (It purely depends upon the user to define the characteristics) 

2. Objects of built-in type that are immutable are:

- Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
- Strings
- Tuples
- Frozen Sets
- User-Defined Classes (It purely depends upon the user to define the characteristics)

https://www.mygreatlearning.com/blog/understanding-mutable-and-immutable-in-python/#:~:text=Mutable%20is%20a%20fancy%20way,once%20it%20has%20been%20created.

### Types of django Field

https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.Field


- AutoField : IntegerField, auto increments IDs

- BigAutoField : A 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.

- BooleanField : The default value of BooleanField is None when Field.default isn’t defined.

- FloatField vs. DecimalField
The FloatField class is sometimes mixed up with the DecimalField class. 
Although they both represent real numbers, they represent those numbers differently. 
FloatField uses Python’s float type internally, while DecimalField uses Python’s Decimal type. 
For information on the difference between the two, see Python’s documentation for the decimal module.

FileField
FilePathField
ImageField

기타 등등

### QureySet and Object

A QuerySet is a collection of data from a database.

**A QuerySet is built up as a list of objects.**

QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data.


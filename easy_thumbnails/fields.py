from django.db.models.fields.files import FileField, ImageField
from easy_thumbnails import files


class ThumbnailerField(FileField):
    """
    A file field which provides easier access for retrieving (and generating)
    thumbnails.

    To use a different file storage for thumbnails, provide the
    ``thumbnail_storage`` keyword argument.
    """
    attr_class = files.ThumbnailerFieldFile

    def __init__(self, *args, **kwargs):
        # Arguments not explicitly defined so that the normal ImageField
        # positional arguments can be used.
        self.thumbnail_storage = kwargs.pop('thumbnail_storage', None)

        super(ThumbnailerField, self).__init__(*args, **kwargs)

    def south_field_triple(self):
        """
        Return a suitable description of this field for South.
        """
        from south.modelsinspector import introspector
        field_class = 'django.db.models.fields.files.FileField'
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)


class ThumbnailerImageField(ThumbnailerField, ImageField):
    """
    An image field which provides easier access for retrieving (and generating)
    thumbnails.

    To use a different file storage for thumbnails, provide the
    ``thumbnail_storage`` keyword argument.

    To thumbnail the original source image before saving, provide the
    ``resize_source`` keyword argument, passing it a usual thumbnail option
    dictionary. For example::

        ThumbnailerImageField(
            ..., resize_source=dict(size=(100, 100), sharpen=True))
    """
    attr_class = files.ThumbnailerImageFieldFile

    def __init__(self, *args, **kwargs):
        # Arguments not explicitly defined so that the normal ImageField
        # positional arguments can be used.
        self.resize_source = kwargs.pop('resize_source', None)

        super(ThumbnailerImageField, self).__init__(*args, **kwargs)

    def south_field_triple(self):
        """
        Return a suitable description of this field for South.
        """
        from south.modelsinspector import introspector
        field_class = 'django.db.models.fields.files.ImageField'
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)


class ThumbnailerCacheImageField(ThumbnailerImageField):
    
    attr_class = files.ThumbnailerCacheImageFieldFile
    
    def __init__(self, thumbnail_cache_field=None, *args, **kwargs):
        self.thumbnail_cache_field = thumbnail_cache_field
        super(ThumbnailerCacheImageField, self).__init__(*args, **kwargs)
    
    
    '''
    def south_field_triple(self):
        """
        Return a suitable description of this field for South.
        """
        from south.modelsinspector import introspector
        field_class = 'django.db.models.fields.files.ImageField'
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)
    
    
    
    def contribute_to_class(self, cls, name):
        super(ImageField, self).contribute_to_class(cls, name)
        # Attach update_dimension_fields so that dimension fields declared
        # after their corresponding image field don't stay cleared by
        # Model.__init__, see bug #11196.
        from easy_thumbnails.signals import thumbnail_created
        thumbnail_created.connect(self.update_thumbnail_cache)
    
        
    def update_thumbnail_cache(self, *args, **kwargs):
        
        print kwargs
        # Update the thumbnail cache field.
        #if self.thumbnail_cache_field:
        #    jsonfield = getattr(instance, self.thumbnail_cache_field)
        #    jsonfield[option_string] = url
        
        thumbnail = kwargs['sender']
    '''    
        
        
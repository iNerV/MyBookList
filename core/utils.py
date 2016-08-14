def image_to(instance, filename, image_size_type):
    folder = instance.__class__.__name__
    if instance.__class__.__name__ == 'Edition':
        folder = 'books'
        instance.fk = instance.summary_id
    elif instance.__class__.__name__ == 'AuthorPhoto':
        folder = 'authors'
        instance.fk = instance.author_id
    elif instance.__class__.__name__ == 'CoverOfPublisher':
        folder = 'publishers'
        instance.fk = instance.publisher_id

    if image_size_type:
        size = '/{}'.format(image_size_type)
    else:
        size = ''
    return '{0}/{1}{2}/{3}'.format(folder.lower(), instance.fk, size, filename)
def image_upload_location(instance, filename):
    return 'media/AppProductos/images/%s.png' % (instance.id)
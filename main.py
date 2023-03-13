from facebook import Facebook

facebook = Facebook()

media_ids = []

image_1 = "https://your_bublic_domain.com/youimage_url.png"
response = facebook.post_image(media_url=image_1)

media_ids.append(response['id'])

image_2 = "https://your_bublic_domain.com/youimage_url.png"
response = facebook.post_image(media_url=image_1)
media_ids.append(response['id'])

response = facebook.create_carousel(ids=media_ids, caption="My first instagram carousel")

container_id = response['id']
    
facebook.publish_media(container_id=container_id)

#done




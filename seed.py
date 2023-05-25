from models import db, User, Post, Tag, PostTag
from app import create_and_configure_app

app = create_and_configure_app()

with app.app_context():
    # Create the database tables
    db.create_all()

    # Create initial users
    user1 = User(first_name='John', last_name='Doe', image_url='https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg')
    user2 = User(first_name='Jane', last_name='Smith', image_url='https://img.freepik.com/premium-vector/portrait-beautiful-young-woman-with-short-wavy-hair_478440-368.jpg')

    # Create initial tags
    tag1 = Tag(name='Fun')
    tag2 = Tag(name='Work')

    # Create initial posts for user1
    post1 = Post(title='First Post', content='Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto explicabo enim voluptas. Atque ut, obcaecati repudiandae, expedita neque porro fugiat ipsum eos dolor similique natus laboriosam, esse deleniti inventore quam. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Recusandae sequi debitis iure veniam itaque excepturi nam rem, quis repellendus, fugit, vel nobis at quae eum corrupti accusamus soluta a? Vero.Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto explicabo enim voluptas. Atque ut, obcaecati repudiandae, expedita neque porro fugiat ipsum eos dolor similique natus laboriosam, esse deleniti inventore quam. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Recusandae sequi debitis iure veniam itaque excepturi nam rem, quis repellendus, fugit, vel nobis at quae eum corrupti accusamus soluta a? Vero.', user=user1)
    post2 = Post(title='Second Post', content='Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto explicabo enim voluptas. Atque ut, obcaecati repudiandae, expedita neque porro fugiat ipsum eos dolor similique natus laboriosam, esse deleniti inventore quam. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Recusandae sequi debitis iure veniam itaque excepturi nam rem, quis repellendus, fugit, vel nobis at quae eum corrupti accusamus soluta a? Vero.', user=user1)

    # Create initial posts for user2
    post3 = Post(title='Hello World', content='This is the first post by Jane Smith. Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto explicabo enim voluptas. Atque ut, obcaecati repudiandae, expedita neque porro fugiat ipsum eos dolor similique natus laboriosam, esse deleniti inventore quam. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Recusandae sequi debitis iure veniam itaque excepturi nam rem, quis repellendus, fugit, vel nobis at quae eum corrupti accusamus soluta a? Vero.', user=user2)

    # Associate tags with posts
    post1.tags.append(tag1)
    post2.tags.extend([tag1, tag2])
    post3.tags.append(tag2)

    # Add users, tags, posts, and post-tag relationships to the session
    db.session.add_all([user1, user2, tag1, tag2, post1, post2, post3])
    db.session.commit()

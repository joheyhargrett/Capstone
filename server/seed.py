# Standard library imports
from random import randint, choice
from models import Customer, Review, Product, OrderedItem, db
from datetime import datetime

# Remote library imports
from faker import Faker

# Local imports
from app import app
from config import bcrypt

with app.app_context():
    fake = Faker()
    
    print("Deleting data...")
    
    Customer.query.delete()
    Product.query.delete()
    Review.query.delete()
    OrderedItem.query.delete()

    def format_phone_number(raw_phone):
        return f"({raw_phone[0:3]}) {raw_phone[3:6]}-{raw_phone[6:]}"

    ratings_and_comments = [
    (5, "Excellent product, exceeded my expectations!"),
    (4, "Fast shipping and great customer service."),
    (1, "Not as described. Very disappointed."),
    (5, "Highly recommended! Will buy again."),
    (5, "The quality is unmatched. Very satisfied."),
    (2, "Poor packaging, item arrived damaged."),
    (5, "Exactly what I needed. Thank you!"),
    (2, "Product didn't meet my expectations."),
    (4, "Amazing value for the price!"),
    (3, "Item arrived on time, but with minor flaws."),
    (5, "Outstanding quality and craftsmanship."),
    (1, "Terrible experience. Avoid this product."),
    (4, "Prompt delivery and hassle-free return process."),
    (3, "Good product, but a bit overpriced."),
    (5, "Superb customer support. Resolved my issue quickly."),
    (2, "Average product. Nothing special."),
    (4, "Great value for money. Would recommend."),
    (2, "The color doesn't match the picture online."),
    (5, "Perfect fit and excellent build quality."),
    (1, "Disappointing purchase. Won't buy again."),
    (3, "Impressed with the product quality."),
    (4, "Fast and reliable shipping service."),
    (1, "Worst purchase ever. Regret buying."),
    (5, "Absolutely love this product!"),
    (3, "Decent product, but not outstanding."),
    (4, "Good experience overall. Will shop again."),
    (2, "Shipping took longer than expected."),
    (5, "Top-notch customer service."),
    (1, "Misleading product description."),
    (3, "Satisfactory purchase. Could be better."),
    (4, "Well-packaged and arrived in perfect condition."),
    (2, "Product had minor defects."),
    (5, "Exemplary quality and craftsmanship."),
    (1, "Received the wrong item. Very frustrating."),
    (3, "Average product for the price."),
    (4, "Happy with the purchase. Would recommend."),
    (2, "Difficulties with the return process."),
    (5, "Amazing product! Worth every penny."),
    (1, "Never buying from this seller again."),
    (3, "Met my expectations. Nothing extraordinary."),
    (4, "Excellent service and product."),
    (2, "Product broke after a short period."),
    (5, "Absolutely fantastic! No complaints."),
    (1, "Regretting this purchase. Poor quality."),
    (3, "Fair product for the price."),
    (4, "Great value and quality."),
    (2, "Customer service needs improvement."),
    (5, "Thrilled with my purchase!"),
    ]
    
    

    new_products = [
    {
        "name": "St. John's Bay Pique Big and Tall Mens Regular Fit Short Sleeve Polo Shirt",
        "description": "This St. John's Bay men's big and tall polo shirt is a stylish go-to for everyday activities. Made from a soft stretch-cotton blend with recycled fabric, this regular-fit short-sleeve style has a collared neck and a two-button closure. Wear it with jeans and boat shoes.",
        "image_url": "https://jcpenney.scene7.com/is/image/JCPenney/DP0421202209012742M?hei=550&wid=550&op_usm=.4%2C.8%2C0%2C0&resmode=sharp2&op_sharpen=1",
        "price": 21.99,
        "stock_quantity": 40,
        "category": "men's clothes"
    },
    {
        "name": "St. John's Bay Pique Big and Tall Mens Regular Fit Short Sleeve Polo Shirt",
        "description": "This St. John's Bay men's big and tall polo shirt is a stylish go-to for everyday activities. Made from a soft stretch-cotton blend with recycled fabric, this regular-fit short-sleeve style has a collared neck and a two-button closure. Wear it with jeans and boat shoes.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/2/optimized/24103162_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 88.49,
        "stock_quantity": 20,
        "category": "men's clothes"
    },
    {
        "name": "Men's Cotton Crewneck Sweater",
        "description": "Polo Ralph Lauren's sweater will keep you comfortably warm when the mercury drops, thanks to its soft, breathable cotton.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/8/optimized/22814998_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1",
        "price": 79.99,
        "stock_quantity": 40,
        "category": "men's clothes"
    },
    {
        "name": "Men's Modern-Fit Stretch Corduroy Solid Sport Coat",
        "description": "Whether you're dressing up a pair of jeans or adding a layer of sophistication to your business-ready look, the streamlined silhouette and unrestrictive stretch performance of this blazer from Michael Kors make it the perfect choice for professional style and comfort.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/7/optimized/24033717_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 79.99,
        "stock_quantity": 15,
        "category": "men's clothes"
    },
    {
        "name": "Men's Slim-Fit Raglan Sport Coat",
        "description": "Bring some raglan-infused energy to your semi-formal look with this slim-fit sport coat from Tallia, the perfect blend of casual and elegant and an effortless pair with button-downs and T-shirts alike.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/5/optimized/24040935_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 74.99,
        "stock_quantity": 12,
        "category": "men's clothes"
    },
    {
        "name": "POLO RALPH LAUREN Men's Classic-Fit Soft Cotton Polo",
        "description": "An American style standard since 1972, the Polo shirt has been imitated but never matched. Over the decades, Ralph Lauren has reimagined his signature style in a wide array of colors and fits, yet all retain the quality and attention to detail of the iconic original. This long-sleeve version is made from luxe cotton interlock with an ultrasoft finish.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/5/optimized/25752915_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 69.99,
        "stock_quantity": 20,
        "category": "men's clothes"
    },
    {
        "name": "POLO RALPH LAUREN Men's Custom Slim Fit Mesh Polo",
        "description": "An American style standard since 1972, the Polo shirt has been imitated but never matched. Over the decades, Ralph Lauren has reimagined his signature style in a wide array of colors and fits, yet all retain the quality and attention to detail of the iconic original. Polo Ralph Lauren's trim version is made from highly breathable cotton mesh, which offers a textured look and a soft feel.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/2/optimized/26328262_fpx.tif?op_sharpen=1&wid=1200&fit=fit,1&$filtersm$&fmt=webp",
        "price": 109.99,
        "stock_quantity": 28,
        "category": "men's clothes"
    },
    {
        "name": "NIKE Men's Totality Dri-FIT Tapered Versatile Pants",
        "description": "Designed for running, training and yoga, these Nike pants are all about versatility. From beginning a new workout routine to pushing your limits in the gym, these lightweight knit pants keep everything simple and fresh.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/0/optimized/25397780_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 54.99,
        "stock_quantity": 15,
        "category": "men's clothes"
    },
    {
        "name": "Men's Apt. 9® Premier Flex Solid Regular-Fit Wrinkle Resistant Dress Shirt",
        "description": "For a sophisticated look that won't soon be forgotten, this men's dress shirt from Apt. 9 features a polished look and fit.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6422263_Light_Blue?wid=805&hei=805&op_sharpen=1",
        "price": 44.99,
        "stock_quantity": 30,
        "category": "men's clothes"
    },
    {
        "name": "Big & Tall Sonoma Goods For Life® Modern-Fit Thermal Crewneck Pullover",
        "description": "Have it all. Featuring a modern fit and thermal construction, this Sonoma Goods For Life crewneck pullover keeps you looking and feeling great.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/3748384_Copenhagen?wid=805&hei=805&op_sharpen=1",
        "price": 11.99,
        "stock_quantity": 65,
        "category": "men's clothes"
    },
    {
        "name": "Men's Apt. 9® Slim-Fit Performance Wrinkle Resistant Dress Shirt",
        "price": 21.99,
        "description": "Fashion forward. Make a stylish statement in this men's Apt. 9 button-down shirt featuring a slim-fit design. HEIQ Smart Temp helps maintain core body temperature.",
        "category": "men's clothes",
        "stock_quantity": 35,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/3710825_Ditsy_Maroon?wid=805&hei=805&op_sharpen=1"
    },
    {
        "name": "Men's Apt. 9® Premier Flex Performance Slim-Fit Washable Suit Jacket",
        "price": 119.99,
        "description": "Unforgettable style. Featuring a modern look and slim fit, this men's Apt. 9 suit jacket will have them remembering you.",
        "category": "men's clothes",
        "stock_quantity": 45,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/5012088_ALT2?wid=1500&hei=1500&op_sharpen=1&qlt=60"
    },
    {
        "name": "Men's Levi's® 505™ Eco-Ease Regular-Fit Stretch Jeans",
        "price": 69.99,
        "description": "Look and feel great in these men's Levi's jeans. Stretch fabric delivers constant comfort.",
        "category": "men's clothes",
        "stock_quantity": 45,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/4806802_Fremont_Drop_Shot?wid=805&hei=805&op_sharpen=1"
    },
    {
        "name": "Men's Sonoma Goods For Life® Bootcut Jeans",
        "price": 29.99,
        "description": "Keep your casual look on trend with these men's Sonoma Goods For Life bootcut jeans.",
        "category": "men's clothes",
        "stock_quantity": 50,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/5860775_ALT4?wid=1500&hei=1500&op_sharpen=1&qlt=60"
    },
    {
        "name": "Men's Levi's® 559™ Stretch Relaxed Straight Fit Jeans",
        "price": 69.99,
        "description": "Fashion forward. Featuring a relaxed fit and straight-leg design, these men's Levi's jeans deliver stellar style",
        "category": "men's clothes",
        "stock_quantity": 25,
        "image_url":  "https://media.kohlsimg.com/is/image/kohls/2483201_Steely_Blue?wid=805&hei=805&op_sharpen=1"
    },
    {
        "name": "Women's Simply Vera Vera Wang Cable Knit Pullover Sweater",
        "price": 44.99,
        "description": "Be comfy and cozy this fall season with this women's Simply Vera Vera Wang cable knit pullover sweater.",
        "category": "women's clothes",
        "stock_quantity": 15,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6318440_ALT2?wid=1500&hei=1500&op_sharpen=1&qlt=60"
    },
    {
        "name": "Women's LC Lauren Conrad Tiered Midi Skirt",
        "price": 37.99,
        "description": "Step into a stylish look with this women's LC Lauren Conrad tiered midi skirt. A-line silhouette, Tiered hem, Pull-on styling, Fully lined.",
        "category": "women's clothes",
        "stock_quantity": 26,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6340487_ALT60?wid=1500&hei=1500&op_sharpen=1&qlt=60"
    },
    {
        "name": "Off Shoulder Short Sleeve Sundress",
        "price": 36.99,
        "description": "A little bit of lace can make everything beautiful and graceful. The Off Shoulder Short Sleeve Sundress with its lacey rim is the stunning dress that would give you the girl next door look. You can find this magnificent dress in 3 lovely shades: black, white, and wine red. You can pick them out in sizes ranging from XS to 5XL. This pretty dress will make the beautiful you look even more gorgeous. So hurry up and get this dress ASAP.",
        "category": "women's clothes",
        "stock_quantity": 15,
        "image_url": "https://forwomenusa.com/cdn/shop/products/off-shoulder-short-sleeve-sundress-women-dress-forwomenusa-28391985217685.jpg?v=1663780560"
    },
    {
        "name": "Sweet Treat Jumpsuit Yellow",
        "price": 54.99,
        "description": "Elevate your style game with our 'Sweet Treat' jumpsuit in a stunning yellow hue that exudes all the vibes of a vibrant sunset. This eye-catching piece is designed for the woman who loves to make a statement and stand out from the crowd.",
        "category": "women's clothes",
        "stock_quantity": 27,
        "image_url": "https://www.divaboutiqueonline.com/cdn/shop/files/Facetune_26-03-2024-14-37-40_1536x.jpg?v=1711482604"
    },
    {
        "name": "Elegance Pearls Rhinestone Party Dresses",
        "price": 65.99,
        "description": "Looking for something to wear to that special event? Say no more. With our beautiful collection of affordable, trendy party dresses at Elegance Pearls Rhinestone, you'll never have a hard time finding the perfect thing for any occasion. For the woman with discerning tastes, our elegant collection of affordable, trendy party dresses at Elegance Pearls Rhinestone is sure to please. With a wide variety of styles and colors to choose from, you're guaranteed to find that perfect dress that'll have you looking radiant from head to toe.",
        "category": "women's clothes",
        "stock_quantity": 25,
        "image_url": "https://forwomenusa.com/cdn/shop/products/sexy-pearls-rhinestone-party-dresses-women-elegance-nightclub-feather-birthday-dress-long-sleeve-mesh-sheer-bodycon-mini-dress-forwomenusa-37752835080416.jpg?v=1663779180"
    },
    {
        "name": "Do Not Go Mesh Maxi Dress Set Orange",
        "price": 54.99,
        "description": "Get ready to turn heads with this stunning mesh skirt set that exudes autumnal vibes all year long. The mesmerizing leaf print in warm, vibrant hues creates a captivating look that is sure to make a statement.The breezy, sheer fabric of this two-piece set effortlessly drapes over your silhouette, offering a versatile and alluring style for the fashion-forward individual. Constructed with 95% polyester and 5% spandex, this set has the perfect amount of stretch for a comfortable and flattering fit. Complete with an adjustable tie, this set allows you to customize your look to suit your unique style. Whether you're hitting the town or attending a special event, this set is a must-have for the modern fashionista.",
        "category": "women's clothes",
        "stock_quantity": 25,
        "image_url": "https://www.divaboutiqueonline.com/cdn/shop/files/Facetune_30-04-2024-13-52-40_1536x.jpg?v=1714519240"
    },
    {
        "name": "Never Ending Midi Dress Black",
        "price": 64.99,
        "description": "Elevate your evening wardrobe with our stunning black and beige striped bodycon dress, designed to make a statement. This strapless beauty features bold horizontal stripes that perfectly contour your silhouette, offering a sleek and sophisticated look. The seamless design and stretchy fabric ensure a comfortable yet flattering fit, ideal for any upscale event or night out.",
        "category": "women's clothes",
        "stock_quantity": 37,
        "image_url": "https://www.divaboutiqueonline.com/cdn/shop/files/Facetune_14-05-2024-17-09-08_1536x.jpg?v=1715731625"
    },
    {
        "name": "Sequin Night Club Party Midi Dress",
        "price": 55.99,
        "description": "Night club party dresses can be a tricky thing to find, but we've got you covered with the Sequin Night Club Party Midi Dress. This dress is made from a stretchy medium-weight fabric that hugs your curves and has an O-neckline, long sleeves, and a sequin design for an edgy style. Pair it with a pair of heels and a clutch for a night on the town.",
        "category": "women's clothes",
        "stock_quantity": 37,
        "image_url": "https://forwomenusa.com/cdn/shop/products/sequin-night-club-party-midi-dress-women-dresses-forwomenusa-33266447286496.jpg?v=1663781044"
    },
    {
        "name": "High Waist Wide Leg Pants For Women",
        "description": "If you are in search of chic and stylish-looking pants, then it’s time to end that hunt. The High Waist Wide Leg Pants for Women is all that you have dreamt about. They are the perfect pair to wear to the office every day. You can find them in 2 different shades: beige and black. It is available in sizes ranging from S to L. Team it up with a nice blouse and a sweet pair of pumps, and you are all good to go. So go get this lovely piece before someone else sweeps it away!",
        "image_url": "https://forwomenusa.com/cdn/shop/products/high-waist-wide-leg-pants-for-women-as-picture-s-forwomenusa-19028151959701.jpg?v=1663779773",
        "price": 29.99,
        "stock_quantity": 20,
        "category": "women's clothes"
    },
    {
        "name": "Sweet Treat Jumpsuit Orange",
        "description": 'Elevate your fashion game with our "Sweet Treat" jumpsuit in a bold and vibrant orange hue. This eye-catching piece is designed for the woman who loves to make a statement and stand out from the crowd. The flattering keyhole neckline and cinched waist accentuate your figure, giving you a sleek and sophisticated silhouette thats impossible to ignore.',
        "image_url": "https://www.divaboutiqueonline.com/cdn/shop/files/Facetune_26-03-2024-14-22-32_1536x.jpg?v=1711482429",
        "price": 54.99,
        "stock_quantity": 20,
        "category": "women's clothes"
    },
    {
        "name": "LAUREN RALPH LAUREN Women's Ruched Stretch Jersey Surplice Dress",
        "description": "The smooth hand of stretch-infused jersey brings ease of movement to this surplice dress from Lauren Ralph Lauren, which is elevated by figure-flattering ruching and a shirred waistband. It's finished with an asymmetrical hem for a contemporary sensibility.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/8/optimized/25912098_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 99.99,
        "stock_quantity": 30,
        'category': "women’s clothes"
    },
    {
        "name": "CALVIN KLEIN Women's Wool Blend Belted Wrap Coat",
        "description": "Effortlessly enviable is all yours in this Calvin Klein wrap coat designed with an asymmetric zip front and a cozy knit bib.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/7/optimized/24248637_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 239.99,
        "stock_quantity": 45,
        "category": "women’s clothes"
    },
    {
        "name": "Women's Metallic Plaid Tweed Blazer",
        "description": "The classic tweed blazer gets a whole new look. Our version features fewer buttons for minimal fuss and a windowpane plaid pattern with a subtle metallic shine. ABOUT THE BRAND: Our new brand was designed for and with women like you. Made for your body, your style, and your truth. As your wardrobe's best friend, these mix-and-match pieces work with everything in your closet.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/4/optimized/25541094_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 59.99,
        "stock_quantity": 30,
        "category": "women's clothes"
    },
    {
        "name": "ADIDAS Women's 3-Stripe Tricot Track Jacket",
        "description": "Dash out the door feeling ready for it all. This track jacket from adidas features raglan sleeves for a distraction-free feel while warming up or recovering later on. Side pockets keep a bus pass and music player within reach.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/9/optimized/22032569_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 54.99,
        "stock_quantity": 53,
        'category': "women’s clothes"
    },
    {
        "name": "Women's Sonoma Goods For Life® Wide-Leg Ankle Jeans",
        "description": "Style made easy. You'll love wearing these women's jeans from Sonoma Goods For Life.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6097539_ALT3?wid=1500&hei=1500&op_sharpen=1&qlt=60",
        "price": 43.99,
        "stock_quantity": 20,
        'category': "women’s clothes"
    },
    {
        "name": "MICHAEL MICHAEL KORS Women's Belted Faux-Fur-Trim Hooded Puffer Coat",
        "description": "MICHAEL Michael Kors' sporty puffer coat is designed with faux-fur trim around the hood and a removable belt. Thumbhole cuffs complete the look.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/9/optimized/24559429_fpx.tif?op_sharpen=1&wid=1200&fit=fit,1&$filtersm$&fmt=webp",
        "price": 167.99,
        "stock_quantity": 63,
        "category": "women's clothes"
    },
    {
        "name": "Women's Levi's® 725™ High Rise Bootcut Jeans",
        "description": "These women's Levi's 725 high-rise bootcut jeans are designed to flatter, hold, and lift.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/4438906_ALT3?wid=1500&hei=1500&op_sharpen=1&qlt=60",
        "price": 69.99,
        "stock_quantity": 15,
        'category': "women’s clothes"
    },
    {
        "name": "Casual Slim Ripped Jeans For Women",
        "description": "The Casual Slim Ripped Jeans for Women will be perfect to be the one you wear any time with anything. This pair of jeans is super comfortable, and its tight fit helps in flaunting that beautiful figure. It comes with suspenders. They are available in the denim blue shade. You can find them in sizes ranging from S to XXL. So get this pair of jeans right now and make your life comfortable!",
        "image_url": "https://forwomenusa.com/cdn/shop/products/casual-slim-ripped-jeans-for-women-women-jeans-forwomenusa-36724210696416.jpg?v=1663778880",
        "price": 39.99,
        "stock_quantity": 30,
        'category': "women’s clothes"
    },
    {
        "name": "Skinny Butt Lift Ripped Jeans",
        "description": "If you're looking for a pair of jeans that will enhance your figure and keep you stylish at the same time, then Skinny Butt Lift Ripped Jeans are the perfect choice for you. Made from premium quality cotton, these jeans are both comfortable and durable, ensuring that you'll be able to wear them time and time again. The high waist design of these jeans provides a flattering and slimming effect, while the skinny fit hugs your curves and accentuates your natural curves.",
        "image_url": "https://forwomenusa.com/cdn/shop/products/skinny-butt-lift-ripped-jeans-women-jeans-blue-s-china-forwomenusa-38583452664032.jpg?v=1675215831",
        "price": 47.89,
        "stock_quantity": 63,
        'category': "women’s clothes"
    },
    {
        "name": "Just For You Ripped Non Stretch Straight Leg Jean",
        "price": 27.99,
        "description": "Pop in this oversized denim jacket and be ready to go. With it's classic medium wash, figure hugging waist and oversized chest fabric for a layered look. Pair with a cute dress or rock with your everyday jeans",
        "category": "women's clothes",
        "stock_quantity": 40,
        "image_url": "https://www.fashionnova.com/cdn/shop/products/03-02-23Studio1_TH_B_10-32-03_27_FN24598FT36_LightWash_5871_EH.jpg?v=1678224286"
    },
    {
        "name": "Ring My Bells Bell Bottom Flare Jeans - Light Wash",
        "price": 69.99,
        "description": "Ring bae's bells, ring my bells bae! Shake things up in our classic Ring My Bell Bottoms! These jeans are perfect for any occasion or any season! If you don't grab the dark wash, be sure to grab the life wash!",
        "category": "women's clothes",
        "stock_quantity": 30,
        "image_url": "https://shopswankaposh.com/cdn/shop/files/20231115-352A6927_2500x.jpg?v=1703022508"
    },
    {
        "name": "For Your Thoughts High Rise Skinny Jeans - Medium Wash",
        "price": 59.99,
        "description": "Take a moment and gather your thoughts on these stylish jeans, featuring a high-rise waist. zippered closure, belt loops, front and rear pockets, and a skinny leg fit with distressing at the knees and frayed ankles.",
        "category": "women's clothes",
        "stock_quantity": 15,
        "image_url": "https://shopswankaposh.com/cdn/shop/files/20240308-352A3971_2048x.jpg?v=1709915992"
    },
    {
        "name": "Juniors' SO® BOHO Cardigan",
        "description": "Wrap yourself in cozy vibes with this super soft BOHO cardigan from SO.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6307158_Tan_Fairisle?wid=805&hei=805&op_sharpen=1",
        "price": 34.99,
        "stock_quantity": 20,
        "category": "Teen's clothes"
    },
    {
        "name": "Juniors' SO® Two-Way Zipper Hooded Cardigan Sweater",
        "price": 31.99,
        "description": "You'll simply love the modern look of this juniors' hooded cardigan with a nifty two-way zipper.",
        "category": "Teen's clothes",
        "stock_quantity": 15,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6116544_Black?wid=805&hei=805&op_sharpen=1"
    },
    {
        "name": "Juniors' SO® Long Sleeve Ribbed Square Neck Top",
        "price": 21.99,
        "description": "Take your casual wardrobe to the next level with this long sleeve ribbed square neck juniors' cropped top from SO.",
        "category": "Teen's clothes",
        "stock_quantity": 25,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/5738968_Modern_White?wid=805&hei=805&op_sharpen=1"
    },
    {
        "name": "Boys 8-20 Sonoma Goods For Life® Everyday Raglan Tee in Regular & Husky",
        "price": 9.99,
        "description": "Casual comfort and style are effortless with this kids' everyday raglan tee from Sonoma Goods For Life.",
        "category": "Teen's clothes",
        "stock_quantity": 15,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/5593806_ALT4?wid=1500&hei=1500&op_sharpen=1&qlt=60"
    },
    {
        "name": "Kids 8-20 Nike Club Fleece Hoodie",
        "price": 49.99,
        "description": "Say hello to this Club Fleece Hoodie from Nike, an essential for running, jumping and laughing your way through the year.",
        "category": "Teen's clothes",
        "stock_quantity": 20,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6120527_Black?wid=805&hei=805&op_sharpen=1"
    },
    {
        "name": "Boys 8-20 Teenage Mutant Ninja Turtles Defenders Inc. Graphic Tee",
        "price": 14.99,
        "description": "Give his wardrobe a radical refresh with this boys' Ninja Turtles graphic tee.",
        "category": "Teen's clothes",
        "stock_quantity": 50,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6450693?wid=805&hei=805&op_sharpen=1"
    },
    {
        "name": "Boys 10-16 OppoSuits Groovy Grey Solid Suit",
        "price": 79.99,
        "description": "When he looks good, he feels good, and that's exactly what will happen when your little dude wears this timeless suit. This OppoSuits grey ensemble is both stylish and comfortable, so he'll have the perfect outfit option for any special occasion.",
        "category": "Teen's clothes",
        "stock_quantity": 40,
        "image_url": "https://media.kohlsimg.com/is/image/kohls/3911337?wid=805&hei=805&op_sharpen=1"
    },
    {
        "name": "Corvette Striped Mechanic Shirt",
        "price": 19.99,
        "description": "A classic mechanic-inspired style accented with authentic Corvette patches.",
        "category": "Teen's clothes",
        "stock_quantity": 50,
        "image_url": "https://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dwc96d7690/62371010_102_main.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg"
    },
    {
        "name": "Solid High-Neck Ribbed Midi Dress",
        "price": 22.99,
        "description": "Wherever you go, you're making an entrance in this sleek, stretchy dress. Throw it on with a cute jacket and some casual kicks.",
        "category": "Teen's clothes",
        "stock_quantity": 60,
        "image_url": "https://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dwd6baeccc/81251513_195_alt2.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg"
    },
    {
        "name": "Essentials Full-Zip Hoodie",
        "price": 29.99,
        "description": "The most relaxed, laid-back hoodie in your wardrobe. Get extra cozy and snag our matching joggers, too.",
        "category": "Teen's clothes",
        "stock_quantity": 80,
        "image_url": "https://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dw2e34693b/81994430_223_alt1.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg"
    },
    {
        "name": "Relaxed Cargo Jean",
        "price": 34.99,
        "description": "A relaxed pair with your most-loved detail: cargo pockets. Fabric features recycled cotton, which is crafted from a mix of pre-and post-consumer waste to help reduce landfills.",
        "category": "Teen's clothes",
        "stock_quantity": 13,
        "image_url": "https://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dw336bef52/64193761_176_alt1.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg"
    },

    {
        "name": "Airwalk French Terry Graphic Joggers",
        "price": 15.99,
        "description": "This French terry pair of joggers features an 'Airwalk' leg graphic, contrasting drawstring at the waist, on-seam side pockets, and elasticized trim.",
        "category": "Teen's clothes",
        "stock_quantity": 96,
        "image_url": "https://www.forever21.com/dw/image/v2/BFKH_PRD/on/demandware.static/-/Sites-f21-master-catalog/default/dw8329a353/1_front_750/00462624-01.jpg?sw=1000&sh=1500"
    },
    {
        "name": "Aero Circle Pullover Hoodie",
        "price": 14.99,
        "description": "A seriously comfy hoodie for everyday lounging. Looks perfect with our matching sweats!",
        "category": "Teen's clothes",
        "stock_quantity": 50,
        "image_url": "https://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dwc057d727/81063331_268_alt1.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg"
    },
    {
        "name": "OAKLAND VARSITY PRINTED OVERSIZED SWEATER",
        "price": 24.99,
        "description": "Sitting pretty at the top of our wishlist, reach comfort heaven this season in this sweatshirt from our latest collection...",
        "category": "Teen's clothes",
        "stock_quantity": 23,
        "image_url": "https://media.boohoo.com/i/boohoo/fzz36832_ecru_xl/female-ecru-oakland-varsity-printed-oversized-sweater?w=450&qlt=default&fmt.jp2.qlt=70&fmt=auto&sm=fit"
    },
    {
        "name": "Drippin Hoodie - Black/combo",
        "price": 12.99,
        "description": "Model Height: 6'2 - Wearing Large. Big & Tall: Height 6'3- Wearing XXXL...",
        "category": "Teen's clothes",
        "stock_quantity": 40,
        "image_url": "https://www.fashionnova.com/cdn/shop/products/DrippinHoodie-Blackcombo_MER_468x.jpg?v=1618955451"
    },
    {
        "name": "Mini Teenage Mutant Ninja Turtle Set - Black",
        "price": 24.99,
        "description": "Available In Black. Screen Tee Long Sleeve Short Set Teenage Mutant Ninja Turtle Graphic Tee",
        "category": "Teen's clothes",
        "stock_quantity": 60,
        "image_url": "https://www.fashionnova.com/cdn/shop/files/01-02-24_S6_38_NJSBAQ5_Black_RA_AA_13-54-21_69285_PXF_468x.jpg?v=1705437028"
    },
    {
        "name": "Jacquard-knit Cotton Sweate",
        "price": 6.99,
        "description": "Jacquard-knit sweater in soft cotton. Long sleeves and ribbing at neck, cuffs, and hem.",
        "category": "kids clothes",
        "stock_quantity": 50,
        "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F0a%2F41%2F0a41edf3e667dc4613073a0e5e80ec00f6cc9145.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BLOOKBOOK%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url[file:/product/main]"
    },
    {
        "name": "Super Soft Skinny Fit Jeans",
        "price": 19.99,
        "description": "Jeans in flexible, supersoft, superstretch denim for added freedom of movement. Skinny fit through hip, thigh, and leg. Adjustable, elasticized waistband, zip fly with snap fastener, front pockets, and open back pockets.",
        "category": "kids clothes",
        "stock_quantity": 60,
        "image_url": "https://lp2.hm.com/hmgoepprod?set=format%5Bwebp%5D%2Cquality%5B79%5D%2Csource%5B%2F2e%2F61%2F2e61f1567578a528c6a24a98caac0d7e5202dc74.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BLOOKBOOK%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url%5Bfile%3A%2Fproduct%2Fmain%5D"
    },
    {
        "name": "Splash Ink UNSPEAKABLE Letter Print Boys Casual Pullover Hooded Long Sleeve Sweatshirt",
        "price": 12.99,
        "description": "Splash Ink UNSPEAKABLE Letter Print Boys Casual Pullover Hooded Long Sleeve Sweatshirt For Spring Fall, Kids Hoodie Tops Outdoor",
        "category": "kids clothes",
        "stock_quantity": 40,
        "image_url": "https://img.kwcdn.com/thumbnail/s/258f6c87f52415c8da3aa532e4572dcf_020718fb5238.jpg?imageView2/2/w/800/q/70"
    },
    {
        "name": "COLOR BLOCK POLAR SHERPA JACKET",
        "price": 59.99,
        "description": "Stay warm and stylish this winter with the Color Block Polar Sherpa Jacket. This super soft polar fleece piece is perfect for keeping cosy in the cold weather...",
        "category": "kids clothes",
        "stock_quantity": 26,
        "image_url": "https://www.tinycottons.com/media/catalog/product/a/w/aw23-229-m42_6.jpg?quality=90&bg-color=255,255,255&fit=bounds&height=1920&width=1280&canvas=1280:1920"
    },
    {
        "name": "STRIPES BODY",
        "price": 24.99,
        "description": "A cotton is a natural fiber which is sustainable, renewable and biodegradable. Pima is in the top one percent of cotton produced in the world. Twice as strong than regular cotton, it is trusted for its integrity and durability so its use results in longer-lasting products. Also, the farming practices employed comply with environmental and ethical...",
        "category": "kids clothes",
        "stock_quantity": 23,
        "image_url": "https://www.tinycottons.com/media/catalog/product/a/w/aw23-058-m30_5.jpg?quality=90&bg-color=255,255,255&fit=bounds&height=1920&width=1280&canvas=1280:1920"
    },
    {
        "name": "Wild Short Sleeve Kids Tee",
        "price": 32.99,
        "description": "Make your kid the wildest in the pack with this super soft tee! Perfect for any adventure, whether it's exploring the backyard or fighting off dragons. Make your little one look fierce and cool in this rad 'Wild' tee!",
        "category": "kids clothes",
        "stock_quantity": 50,
        "image_url": "https://rags.com/cdn/shop/files/K01B4843.jpg?v=1698172624&width=1400"
    },
    {
        "name": "Camel Check Short Sleeve Kids Essentials Tee",
        "price": 19.99,
        "description": "This super soft kids tee is ready to tackle playtime and look rad at the same time! Our kid’s tee in 'Camel Check' looks awesome for a day out. It's the total package for every trendy kid.",
        "category": "kids clothes",
        "stock_quantity": 40,
        "image_url": "https://rags.com/cdn/shop/files/K01B6897.jpg?v=1699481144&width=1400"
    },
    {
        "name": "Phantom Essentials Short Sleeve Chest Pocket Rounded Kids Tee",
        "price": 19.99,
        "description": "The softness and bold colors kids crave and the durability parents love!...",
        "category": "kids clothes",
        "stock_quantity": 40,
        "image_url": "https://rags.com/cdn/shop/files/K01B3577.jpg?v=1702401241&width=1400"
    },
    {
        "name": "Pink Check Essentials Short Sleeve Rounded Kids Tee",
        "price": 19.99,
        "description": "Show off your kid's cool style with our Essentials Kids Tee in Pink Checker...",
        "category": "kids clothes",
        "stock_quantity": 50,
        "image_url": "https://rags.com/cdn/shop/files/K01B4308_4757c24d-7186-4a41-844f-18abc922c2ae.jpg?v=1698080122&width=1400"
    },
    {
        "name": "Sagebrush Stripe Essentials Long Sleeve Pocket Kids Tee",
        "price": 21.99,
        "description": "The softness your kids crave at a price your wallet will appreciate. Part of our #1 best-selling collection...",
        "category": "kids clothes",
        "stock_quantity": 40,
        "image_url": "https://rags.com/cdn/shop/files/K01B7308_78a8696d-56bc-4f56-b9a3-b928f19f90c3.jpg?v=1697821015&width=1400"
    },
    {
        "name": "Checks & Hearts Short Sleeve Swing Dress",
        "price": 42.99,
        "description": "Get ready for some sweet style this Valentine's Day with our Short Sleeve Swing Dress!...",
        "category": "kids clothes",
        "stock_quantity": 25,
        "image_url": "https://rags.com/cdn/shop/files/K01B9944_92eba006-82ce-41cc-b9a0-26e9a6cc3265.jpg?v=1705197805&width=1400"
    },
    {
        "name": "Rose Pink Essentials Short Sleeve with Chest Pocket Dress",
        "price": 29.99,
        "description": "Unconventional dressing starts with a whole new fit! The Essentials Short Sleeve Dress brings the fun and goes the distance...",
        "category": "kids clothes",
        "stock_quantity": 35,
        "image_url": "https://rags.com/cdn/shop/files/K01B3101.jpg?v=1692900157&width=1400"
    },
    {
        "name": "Camel Kids Essentials Joggers",
        "price": 34.99,
        "description": "Stylish, durable, and versatile. The perfect amount of stretch and comfort will make these your kiddo's new favorite joggers...",
        "category": "kids clothes",
        "stock_quantity": 34,
        "image_url": "https://rags.com/cdn/shop/files/INFANTJOGGERS.png?v=1690391231&width=1400"
    },
    {
        "name": "Brick Red Essentials 3/4 Rolled Sleeve Henley Long Rag Romper",
        "price": 24.99,
        "description": "Part of our #1 best-selling collection, Essentials Rags are your kid's new favorite basics!...",
        "category": "kids clothes",
        "stock_quantity": 25,
        "image_url": "https://rags.com/cdn/shop/files/K01B1748.jpg?v=1696980875&width=1400"
    },
    {
        "name": "Newborn Rag in Phantom Newborn Essentials Peekabooty™ Rag Romper Long Sleeve",
        "price": 25.99,
        "description": "Ahhh, the newborn stage: Full of dozens of diaper and outfit changes. We're here to make life easier for you in those first few months...",
        "category": "kids clothes",
        "stock_quantity": 25,
        "image_url": "https://rags.com/cdn/shop/products/4_1425007b-83a7-4fa8-b567-c830b6148fd6.jpg?v=1695913454&width=1400"
    }
    ]
    
    print("Seeding customers...")
    
    customers = []

    for n in range(50):
        raw_phone_number = fake.numerify(text='##########')
        formatted_phone_number = format_phone_number(raw_phone_number)
        
        
        
        
        customer = Customer(
            first_name=fake.first_name(), 
            last_name=fake.last_name(),
            email=fake.email(),
            address=fake.address(),
            phone_number=formatted_phone_number
        )
        customer.password_hash=fake.password()
        customers.append(customer)
    
    
    
    
    
    
    
    print("Seeding products...")
    
    products = []

    for product_data in new_products:
        product = Product(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            stock_quantity=product_data["stock_quantity"],
            category=product_data["category"],
            image_url=product_data["image_url"]
        )
        products.append(product)
        
        for product in products:
            db.session.add(product)
            db.session.commit()

    print("Seeding reviews...")
    # List to store review instances
    reviews = []
    i = 1

    # Iterate through products and assign random reviews with ratings
    for product in products:
        random_review = choice(ratings_and_comments)
        rating = random_review[0]
        comment = random_review[1]

        review = Review(
            rating=rating,
            comment=comment,
            customer_id=randint(1, 50),  
            product_id=product.id 
        )
        reviews.append(review)
    
    print("Seeding ordered items...")
    ordered_items = []

    for customer in customers:
        product = choice(products)

        ordered_item = OrderedItem(
            quantity=randint(1, 5),  
            customer=customer,  
            product=product, 
            product_id=product.id,
            order_date=fake.date_time_between(
            start_date=datetime(datetime.now().year, 1, 1),
            end_date=datetime.now()
            )
        )

        ordered_items.append(ordered_item)
        
        
        

    db.session.add_all(customers)
    db.session.add_all(products)
    db.session.add_all(ordered_items)
    db.session.add_all(reviews)
    db.session.commit()

    print("Seed completed.")


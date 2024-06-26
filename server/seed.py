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
        "name": "Tommy Hilfiger Men's Modern-Fit Corduroy Sport Coat - Khaki",
        "description": "Elevate your wardrobe with the Tommy Hilfiger Men's Modern-Fit Corduroy Sport Coat in Khaki. This stylish sport coat features a modern fit, offering a sleek and tailored look perfect for any occasion. Made from premium corduroy fabric, it combines comfort and sophistication effortlessly. Ideal for both casual and formal settings, this sport coat is a versatile addition to your collection, embodying the timeless elegance of Tommy Hilfiger.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/2/optimized/24103162_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 189.99,
        "stock_quantity": 20,
        "category": "men's clothes"
    },
    {
        "name": "Tres Chic Poplin Shirt - Blue",
        "description": "Elevate your wardrobe with the Tres Chic Poplin Shirt in Blue, also available in White. This stylish collared shirt features a classic button-down design and a modern dolphin hem. With a slight stretch for added comfort, it’s made from a blend of 65% cotton, 30% nylon, and 5% spandex. Perfect for a chic, polished look that effortlessly transitions from day to night.",
        "image_url": "https://www.fashionnova.com/cdn/shop/products/TresChicPoplinShirt-Blue_MER_468x@2x.jpg?v=1649101280",
        "price": 24.99,
        "stock_quantity": 17,
        "category": "women's clothes"
    },
    {
        "name": "LUX Short Sleeve Button Down",
        "description": "Our best-selling fabric in all new styles. With a structured drape for that always clean, crisp look, our new LUX styles have just the right amount of stretch making these your new go-to from office to night out.",
        "image_url": "https://cdn.shopify.com/s/files/1/1464/5034/files/D4LUXShortSleeveButtonDownWhite_0825.jpg?v=1713473250&width=960&quality=90",
        "price": 59.99,
        "stock_quantity": 15,
        "category": "men's clothes"
    },
    {
        "name": "Drop-Cut: LUX Polo",
        "description": "The sophisticated LUX Polo has everything you need to stay fresh all day long. With cool-touch technology and our iconic drop-cut hemline, you'll be reaching for this Polo every morning.",
        "image_url": "https://cdn.shopify.com/s/files/1/1464/5034/products/LuxPolo-Navy1.jpg?v=1715706020&width=960&quality=90",
        "price": 49.99,
        "stock_quantity": 22,
        "category": "men's clothes"
    },
    {
        "name": "Executive Stretch Short Sleeve",
        "description": "Introducing the Executive Stretch Short Sleeve - the ultimate button-up for the modern professional. Crafted with lightweight, stay-cool fabric, this stretch-fit design is tailored to perfection, so you can step into wherever the day takes you with renewed confidence and ultimate comfort.",
        "image_url": "https://cdn.shopify.com/s/files/1/1464/5034/products/Black_ExecStretch_SS-4.jpg?v=1716324398&width=960&quality=90",
        "price": 79.99,
        "stock_quantity": 15,
        "category": "men's clothes"
    },
    {
        "name": "Drop-Cut: LUX Dotted Polo",
        "description": "The sophisticated LUX Polo has everything you need to stay fresh all day long.  With cool-touch technology and our iconic drop-cut hemline, you'll be reaching for this Polo every morning.",
        "image_url": "https://cdn.shopify.com/s/files/1/1464/5034/products/LUXPOLODOTTED_BONE1_d5bcbdab-ece7-40e5-97af-69723c104109.jpg?v=1692029239&width=960&quality=90",
        "price": 47.99,
        "stock_quantity": 12,
        "category": "men's clothes"
    },
    {
        "name": "American Bazi Distressed Button Down Denim Shirt Jacket",
        "description": "The distressed button-down denim shirt jacket exudes a casual yet rugged style. With its worn-in appearance, it adds a touch of authenticity to any outfit. Whether paired with jeans or layered over a dress, it effortlessly enhances your fashion game. The comfortable fit and durable fabric make it a go-to choice for everyday wear. The unique distressed details give it a vintage-inspired charm that sets it apart from regular denim jackets. Elevate your wardrobe with this versatile and trendy piece now.",
        "image_url": "https://e2gworld.com/cdn/shop/files/6dff7598-d222-4289-8dba-5084f6d1873f-Max_934x1400.jpg?v=1718972165",
        "price": 32.99,
        "stock_quantity": 15,
        "category": "women's clothes"
    },
    {
        "name": "The Everyday Pant 2.0",
        "description": "For those on the move - this versatile style has been improved in every way, the Everyday Pant 2.0 is our answer to your quest for the perfect pant. Now featuring a premium flex-stretch fabrication and all around updated tapered cut, this iconic silhouette brings added comfort and elegance to your wardrobe.",
        "image_url": "https://cdn.shopify.com/s/files/1/1464/5034/files/EVERYDAY-PANT-2.0_Tan_PCUpdate09_ff020adc-3937-495d-af8a-6f64a0fd13ba.jpg?v=1713378970&width=960&quality=90",
        "price": 119.99,
        "stock_quantity": 15,
        "category": "men's clothes"
    },
    {
        "name": "Drop-Cut: BYLT Signature",
        "description": "With all the best features you deserve, you’ve finally found a shirt that doesn’t shrink, doesn’t fade, has breathability, ultra-stretch and holds up wash-after-wash. As the one that started them all, The “BYLT Signature” Fabric takes this a step further with an unmatched level of comfort in its soft-touch feel, a looser drape for ultimate mobility, and natural performance wicking for the best in class daily wear, making this your new go-to for wherever the day takes you.",
        "image_url": "https://cdn.shopify.com/s/files/1/1464/5034/products/White02_62643f8e-223c-4dc9-98e9-c10ca83663cc.jpg?v=1704398525&width=960&quality=90",
        "price": 29.99,
        "stock_quantity": 16,
        "category": "men's clothes"
    },
    {
        "name": "Jaheem African Print Short Sleeve T-shirt (Green Tortoise Back)",
        "description": "The Jaheem African Print Short Sleeve Tee (Green Tortoise Back) elevates your casual wear, creating a more sophisticated ensemble for the refined gentleman. As a transitional piece, sport the tee with a pair of jeans or dress pants. Take advantage of this multipurpose piece, as it is what your wardrobe's been missing! ",
        "image_url": "https://www.diyanu.com/cdn/shop/products/men-s-tops-jaheem-african-print-short-sleeve-t-shirt-green-tortoise-back-1_1000x1400.jpg?v=1548258902",
        "price": 34.99,
        "stock_quantity": 12,
        "category": "men's clothes"
    },
    {
        "name": "Elite+ Fairway Drop-Cut Pullover",
        "description": "With its magnetic seam system, this pullover design allows for a unique solution to ultimate mobility. Large double hidden interior pockets provide a low profile versatility for those on the go. Made complete with the soft herringbone contrast collar, this pullover is the perfect layering piece for a truly sophisticated style. ",
        "image_url": "https://cdn.shopify.com/s/files/1/1464/5034/products/Fairway-Storm1.jpg?v=1716245346&width=960&quality=90",
        "price": 99.99,
        "stock_quantity": 19,
        "category": "men's clothes"
    },
    {
        "name": "Adil Men's Traditional Dress Pants with Drawstring (White)",
        "description": "Stretch the Summer! Our Adil drawstring pants are the perfect one-color coordinate for our multi-hued new collection. Lithe and lustrous in white stretch cotton sateen, they pair strikingly with any of our traditional tops, applique T-shirts or button-up short sleeves. The sleek cut works for just about any summer occasion, from poolside to cook-out.",
        "image_url": "https://www.diyanu.com/cdn/shop/products/Mens-Adil-pants-white3_971x1371.jpg?v=1652718560",
        "price": 64.99,
        "stock_quantity": 12,
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
        "name": "Rammy Men's African Print Blazer (Black Brown Geometric)",
        "description": "Be stylish and unique at your next formal event in our Rammy African print blazer jacket!",
        "image_url": "https://www.diyanu.com/cdn/shop/files/jackets-rammy-men-s-african-print-blazer-black-brown-geometric-3_1_1000x1400.jpg?v=1713274765",
        "price": 112.99,
        "stock_quantity": 25,
        "category": "men's clothes"
    },
    {
        "name": "Asan Men's Linen Blend Pants (Sand)",
        "description": "Embrace the warmth of the season with our Asan Linen Blend Pants in Sand. These pants are the ideal color for our vibrant new collection, offering a solid base to match any look. Made from lightweight, breathable linen, you'll have comfort and style for any summer outing, from beach days to evening barbecues. ",
        "image_url": "https://www.diyanu.com/cdn/shop/files/Mens-Ajisomo-AfricanPrint-Tunic-WhiteOliveTribal12_d2e0e98a-ccaa-4de5-8ee1-ce7cd0325b04_620x868.jpg?v=1715104059",
        "price": 64.99,
        "stock_quantity": 12,
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
        "description": "Fashion forward. Make a stylish statement in this men's Apt. 9 button-down shirt featuring a slim-fit design. HEIQ Smart Temp helps maintain core body temperature.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/3710825_Ditsy_Maroon?wid=805&hei=805&op_sharpen=1",
        "price": 21.99,
        "stock_quantity": 35,
        "category": "men's clothes"
    },
    {
        "name": "Men's Apt. 9® Premier Flex Performance Slim-Fit Washable Suit Jacket",
        "description": "Unforgettable style. Featuring a modern look and slim fit, this men's Apt. 9 suit jacket will have them remembering you.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/5012088_ALT2?wid=1500&hei=1500&op_sharpen=1&qlt=60",
        "price": 119.99,
        "stock_quantity": 45,
        "category": "men's clothes"
    },
    {
        "name": "Men's Levi's® 505™ Eco-Ease Regular-Fit Stretch Jeans",
        "description": "Look and feel great in these men's Levi's jeans. Stretch fabric delivers constant comfort.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/4806802_Fremont_Drop_Shot?wid=805&hei=805&op_sharpen=1",
        "price": 69.99,
        "stock_quantity": 45,
        "category": "men's clothes"
    },
    {
        "name": "Men's Sonoma Goods For Life® Bootcut Jeans",
        "description": "Keep your casual look on trend with these men's Sonoma Goods For Life bootcut jeans.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/5860775_ALT4?wid=1500&hei=1500&op_sharpen=1&qlt=60",
        "price": 29.99,
        "stock_quantity": 50,
        "category": "men's clothes"
    },
    {
        "name": "Men's Levi's® 559™ Stretch Relaxed Straight Fit Jeans",
        "description": "Fashion forward. Featuring a relaxed fit and straight-leg design, these men's Levi's jeans deliver stellar style",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/2483201_Steely_Blue?wid=805&hei=805&op_sharpen=1",
        "price": 69.99,
        "stock_quantity": 25,
        "category": "men's clothes"
    },
    {
        "name": "Haptics Floral Crochet Side Slit Knit Top",
        "description": "This floral crochet side slit knit top is a beautiful and elegant addition to your wardrobe. The floral crochet detail adds a touch of femininity and charm to the classic knit design. With side slits for added style and movement, this top is perfect for both casual and dressy occasions. The lightweight knit material makes it comfortable to wear all day long. Pair it with your favorite jeans or skirt for a stylish and effortless look. Make a statement with this chic and versatile top that effortlessly combines sophistication with a hint of floral flair.",
        "image_url": "https://e2gworld.com/cdn/shop/files/477204d8-b7ab-4d37-8a07-f4bbc9f31c89-Max_1000x1500.jpg?v=1718897489",
        "price": 34.99,
        "stock_quantity": 30,
        "category": "women's clothes"
    },
    {
        "name": "Cotton Men’s Cardigan",
        "description": "Supremely soft with intricate cable knit, this gorgeous shawl collar cardigan is made from plush organic cotton with a touch of luxurious linen to layer from season to season.",
        "image_url": "https://i0.wp.com/guiltyfashionboutique.com/wp-content/uploads/2024/05/facetune_22-04-2024-21-47-06.jpeg?fit=1440%2C1920&ssl=1",
        "price": 64.99,
        "stock_quantity": 12,
        "category": "men's clothes"
    },
    {
        "name": "Women's Simply Vera Vera Wang Cable Knit Pullover Sweater",
        "description": "Be comfy and cozy this fall season with this women's Simply Vera Vera Wang cable knit pullover sweater.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6318440_ALT2?wid=1500&hei=1500&op_sharpen=1&qlt=60",
        "price": 44.99,
        "stock_quantity": 15,
        "category": "women's clothes"
    },
    {
        "name": "Women's LC Lauren Conrad Tiered Midi Skirt",
        "description": "Step into a stylish look with this women's LC Lauren Conrad tiered midi skirt. A-line silhouette, Tiered hem, Pull-on styling, Fully lined.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6340487_ALT60?wid=1500&hei=1500&op_sharpen=1&qlt=60",
        "price": 37.99,
        "stock_quantity": 26,
        "category": "women's clothes"
    },
    {
        "name": "ATHLETIC FIT STRETCH SUIT PANTS - HEATHERED LIGHT BLUE",
        "description": "Built on the forefront of fit, comfort, and a professional look - these are the perfect dress pants for guys with athletic legs. The fit is built for guys who need more room in the seat, thighs, and quads while still looking to achieve a tapered look. The insane amount of stretch in these slacks allow them to be worn tailored without sacrificing comfort.",
        "image_url": "https://sfycdn.speedsize.com/2780c694-3419-4266-9652-d242439affeb/https://stateandliberty.com/cdn/shop/files/BlakeCashmanHLB3_7579ae99-f8b0-463f-b050-dbd04ca68186.jpg?v=1700680911&width=800",
        "price": 79.99,
        "stock_quantity": 18,
        "category": "men's clothes"
    },
    {
        "name": "Rashida Women's Stretch Dress (Black)",
        "description": "The Rashida Women's Stretch Dress in Black captivates with its off-the-shoulder design, blending sleek sophistication with understated elegance. Its form-fitting stretch fabric ensures a stunning silhouette, while the unique neckline adds a touch of allure. ",
        "image_url": "https://www.diyanu.com/cdn/shop/files/RashidaWomen_sAfricanPrintStretchDress_Black_-5_c9b2bd7c-57e2-4af3-9f0c-c9a538817f0f_800x.jpg?v=1716320718",
        "price": 59.99,
        "stock_quantity": 26,
        "category": "women's clothes"
    },
    {
        "name": "Strapless Raw Edge Harem Leg Denim Jumpsuit",
        "description": "Embrace effortless style with our Strapless Raw Edge Harem Leg Denim Jumpsuit. Featuring a chic strapless design with a boat neckline, this jumpsuit offers a modern and relaxed fit. The pockets and raw edge details add a touch of edgy flair, while the harem leg design ensures comfort and a unique silhouette. Crafted from durable denim fabric, this jumpsuit is perfect for casual outings and stylish gatherings alike.",
        "image_url": "https://img.staticdj.com/9ac6dc73260c022dbcb097188d8ac631_750x.png",
        "price": 49.99,
        "stock_quantity": 6,
        "category": "women's clothes"
    },
    {
        "name": "Floral Print Colorblock Vacation Shorts Matching Set",
        "description": "Step into vacation mode with our Floral Print Colorblock Short Sleeve Blouse and Shorts Matching Set. This regular silhouette set features a chic turndown collar and short sleeves, perfect for warm-weather getaways. The vibrant floral print and colorblock design add a stylish touch, while the comfortable polyester fabric ensures a relaxed fit. Ideal for casual outings or beachside strolls, this set is a must-have for your vacation wardrobe.",
        "image_url": "https://img.staticdj.com/aaa030408dfb522a3d58374a46274eca_750x.png",
        "price": 35.99,
        "stock_quantity": 21,
        "category": "women's clothes"
    },
    {
        "name": "Culture Code Full Size Ribbed Zip Up Drawstring Hooded Jacket",
        "description": "This jacket is a trendy and versatile piece that adds a touch of texture to any outfit. With its zip closure and adjustable drawstring hood, it offers both style and functionality.",
        "image_url": "https://e2gworld.com/cdn/shop/files/95b69071-d0da-40a6-a226-8901c2812ed2-Max_934x1400.jpg?v=1718972132",
        "price": 29.99,
        "stock_quantity": 25,
        "category": "women's clothes"
    },
    {
        "name": "Off Shoulder Short Sleeve Sundress",
        "description": "A little bit of lace can make everything beautiful and graceful. The Off Shoulder Short Sleeve Sundress with its lacey rim is the stunning dress that would give you the girl next door look. You can find this magnificent dress in 3 lovely shades: black, white, and wine red. You can pick them out in sizes ranging from XS to 5XL. This pretty dress will make the beautiful you look even more gorgeous. So hurry up and get this dress ASAP.",
        "image_url": "https://forwomenusa.com/cdn/shop/products/off-shoulder-short-sleeve-sundress-women-dress-forwomenusa-28391985217685.jpg?v=1663780560",
        "price": 36.99,
        "stock_quantity": 15,
        "category": "women's clothes"
    },
    {
        "name": "Sweet Treat Jumpsuit Yellow",
        "description": "Elevate your style game with our 'Sweet Treat' jumpsuit in a stunning yellow hue that exudes all the vibes of a vibrant sunset. This eye-catching piece is designed for the woman who loves to make a statement and stand out from the crowd.",
        "image_url": "https://www.divaboutiqueonline.com/cdn/shop/files/Facetune_26-03-2024-14-37-40_1536x.jpg?v=1711482604",
        "price": 54.99,
        "stock_quantity": 27,
        "category": "women's clothes"
    },
    {
        "name": "Elegance Pearls Rhinestone Party Dresses",
        "description": "Looking for something to wear to that special event? Say no more. With our beautiful collection of affordable, trendy party dresses at Elegance Pearls Rhinestone, you'll never have a hard time finding the perfect thing for any occasion. For the woman with discerning tastes, our elegant collection of affordable, trendy party dresses at Elegance Pearls Rhinestone is sure to please. With a wide variety of styles and colors to choose from, you're guaranteed to find that perfect dress that'll have you looking radiant from head to toe.",
        "image_url": "https://forwomenusa.com/cdn/shop/products/sexy-pearls-rhinestone-party-dresses-women-elegance-nightclub-feather-birthday-dress-long-sleeve-mesh-sheer-bodycon-mini-dress-forwomenusa-37752835080416.jpg?v=1663779180",
        "price": 65.99,
        "stock_quantity": 25,
        "category": "women's clothes"
    },
    {
        "name": "Ruby Ola Voga Women’s Ribbed Top, Grey",
        "description": "The Ruby women’s top is a must-have for women who like fashionable and comfortable styles. A fitted cut crop top perfectly emphasizes feminine shapes and at the same time ensures full comfort of wearing. Made of high-quality ribbed cotton, it guarantees softness and delicacy of touch. There is a subtle embroidered patch with the OLAVOGA logo on the front, adding a unique character to the whole. This top is perfect for both everyday and special occasions, giving you a stylish look and a sense of self-confidence.",
        "image_url": "https://i0.wp.com/guiltyfashionboutique.com/wp-content/uploads/2024/04/img_6794.jpeg?fit=600%2C800&ssl=1",
        "price": 34.99,
        "stock_quantity": 37,
        "category": "women's clothes"
    },
    {
        "name": "Do Not Go Mesh Maxi Dress Set Orange",
        "description": "Get ready to turn heads with this stunning mesh skirt set that exudes autumnal vibes all year long. The mesmerizing leaf print in warm, vibrant hues creates a captivating look that is sure to make a statement.The breezy, sheer fabric of this two-piece set effortlessly drapes over your silhouette, offering a versatile and alluring style for the fashion-forward individual. Constructed with 95% polyester and 5% spandex, this set has the perfect amount of stretch for a comfortable and flattering fit. Complete with an adjustable tie, this set allows you to customize your look to suit your unique style. Whether you're hitting the town or attending a special event, this set is a must-have for the modern fashionista.",
        "image_url": "https://www.divaboutiqueonline.com/cdn/shop/files/Facetune_30-04-2024-13-52-40_1536x.jpg?v=1714519240",
        "price": 54.99,
        "stock_quantity": 25,
        "category": "women's clothes"
    },
    {
        "name": "Never Ending Midi Dress Black",
        "description": "Elevate your evening wardrobe with our stunning black and beige striped bodycon dress, designed to make a statement. This strapless beauty features bold horizontal stripes that perfectly contour your silhouette, offering a sleek and sophisticated look. The seamless design and stretchy fabric ensure a comfortable yet flattering fit, ideal for any upscale event or night out.",
        "image_url": "https://www.divaboutiqueonline.com/cdn/shop/files/Facetune_14-05-2024-17-09-08_1536x.jpg?v=1715731625",
        "price": 64.99,
        "stock_quantity": 37,
        "category": "women's clothes"
    },
    {
        "name": "Sequin Night Club Party Midi Dress",
        "description": "Night club party dresses can be a tricky thing to find, but we've got you covered with the Sequin Night Club Party Midi Dress. This dress is made from a stretchy medium-weight fabric that hugs your curves and has an O-neckline, long sleeves, and a sequin design for an edgy style. Pair it with a pair of heels and a clutch for a night on the town.",
        "image_url": "https://forwomenusa.com/cdn/shop/products/sequin-night-club-party-midi-dress-women-dresses-forwomenusa-33266447286496.jpg?v=1663781044",
        "price": 55.99,
        "stock_quantity": 37,
        "category": "women's clothes"
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
        "description": "Elevate your fashion game with our 'Sweet Treat' jumpsuit in a bold and vibrant orange hue. This eye-catching piece is designed for the woman who loves to make a statement and stand out from the crowd. The flattering keyhole neckline and cinched waist accentuate your figure, giving you a sleek and sophisticated silhouette thats impossible to ignore.",
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
        "category": "women's clothes"
    },
    {
        "name": "CALVIN KLEIN Women's Wool Blend Belted Wrap Coat",
        "description": "Effortlessly enviable is all yours in this Calvin Klein wrap coat designed with an asymmetric zip front and a cozy knit bib.",
        "image_url": "https://slimages.macysassets.com/is/image/MCY/products/7/optimized/24248637_fpx.tif?op_sharpen=1&wid=700&hei=855&fit=fit,1&fmt=webp",
        "price": 239.99,
        "stock_quantity": 45,
        "category": "women's clothes"
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
        "category": "women's clothes"
    },
    {
        "name": "Women's Sonoma Goods For Life® Wide-Leg Ankle Jeans",
        "description": "Style made easy. You'll love wearing these women's jeans from Sonoma Goods For Life.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6097539_ALT3?wid=1500&hei=1500&op_sharpen=1&qlt=60",
        "price": 43.99,
        "stock_quantity": 20,
        "category": "women's clothes"
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
        "category": "women's clothes"
    },
    {
        "name": "Casual Slim Ripped Jeans For Women",
        "description": "The Casual Slim Ripped Jeans for Women will be perfect to be the one you wear any time with anything. This pair of jeans is super comfortable, and its tight fit helps in flaunting that beautiful figure. It comes with suspenders. They are available in the denim blue shade. You can find them in sizes ranging from S to XXL. So get this pair of jeans right now and make your life comfortable!",
        "image_url": "https://forwomenusa.com/cdn/shop/products/casual-slim-ripped-jeans-for-women-women-jeans-forwomenusa-36724210696416.jpg?v=1663778880",
        "price": 39.99,
        "stock_quantity": 30,
        "category": "women's clothes"
    },
    {
        "name": "Plunge Halter Jogger Jumpsuit",
        "description": "Make a bold fashion statement with this Plunge Halter Jogger Jumpsuit, featuring a plunging neckline and comfortable jogger-style pants. Whether you're dressing up for a night out or seeking a chic yet relaxed look, this jumpsuit combines style and comfort for a versatile and trendy ensemble.",
        "image_url": "https://cdn-review.cupshe.com/cmc-admin/2024_03_11/10_43_221/04381c98-da8b-4796-baf7-e6c2a8f561d5/CAA13E3F043TT/1.jpg?x-oss-process=image/format,avif/quality,q_100/resize,w_1500",
        "price": 31.99,
        "stock_quantity": 19,
        "category": "women's clothes"
    },
    {
        "name": "Royal Blue One Shoulder Romper",
        "description": "Make a bold fashion statement with the Royal Blue One Shoulder Romper, a chic and stylish piece that's perfect for a night out on the town or a sunny day by the beach!",
        "image_url": "https://cdn-review.cupshe.com/cmc-admin/product/20230415/c7d71feb6b9140bbb362ad766dd28237.jpg?x-oss-process=image/format,avif/quality,q_100/resize,w_1500",
        "price": 29.99,
        "stock_quantity": 25,
        "category": "women's clothes"
    },
    {
        "name": "Cutout Textured V-Neck Tee",
        "description": "Make a statement with our Cutout Textured V-Neck Tee. This trendy tee features eye-catching cutout details and a textured fabric for added dimension, perfect for adding a touch of edge to your casual outfits.",
        "image_url": "https://cdn-review.cupshe.com/cmc-admin/product/20240614/c6f02bf00fa2f99d71726c11854ab149.jpg?x-oss-process=image/format,avif/quality,q_100/resize,w_1500",
        "price": 22.99,
        "stock_quantity": 36,
        "category": "women's clothes"
    },
    {
        "name": "Sage Eyelet Jersey Tank Top",
        "description": "The Sage Eyelet Jersey Tank Top keeps you cool and stylish with its breathable jersey fabric and delicate eyelet detailing, making it a perfect summer staple.",
        "image_url": "https://cdn-review.cupshe.com/cmc-admin/2024_03_06/14_05_203/3f0cca2e-4bdf-4954-bc9b-933da36982fe/CAA04A3M006PP/4.jpg?x-oss-process=image/format,avif/quality,q_100/resize,w_1500",
        "price": 22.99,
        "stock_quantity": 21,
        "category": "women's clothes"
    },
    {
        "name": "Time Out Crossover Distressed Vintage Ankle Jeans - Light Blue Wash",
        "description": "Elevate your casual wardrobe with the Time Out Crossover Distressed Vintage Ankle Jeans in Light Blue Wash. These stylish straight leg jeans feature a distressed vintage look, an 11\" high rise, and a unique notched fray hem. With low stretch for added comfort and durability, they have a classic 5-pocket design and a 27\" inseam. Each pair is uniquely crafted through a specialized distressing and wash process. Made from a blend of 68% cotton, 31% polyester, and 1% spandex. Perfect for adding a touch of vintage flair to any outfit.",
        "image_url": "https://www.fashionnova.com/cdn/shop/products/TimeCrossoverDistressedVintageAnkleJeans-LightBlueWash_MER.jpg?v=1595298723",
        "price": 34.99,
        "stock_quantity": 16,
        "category": "women's clothes"
    },
    {
        "name": "Time Tells Vintage Ankle Jeans - Light Blue Wash",
        "description": "Discover timeless style with the Time Tells Vintage Ankle Jeans in Light Blue Wash. These straight leg jeans offer a low-stretch fit with a vintage look, featuring a distinctive notched fray hem and classic 5-pocket design. The 10.75\" high rise and 27\" inseam provide a flattering fit, perfect for any casual occasion. Each pair is uniquely crafted through a specialized wash process, ensuring one-of-a-kind style. Made from a blend of 67% cotton, 29% polyester, 3% rayon, and 1% spandex. Follow care instructions carefully to maintain the garments aesthetic.",
        "image_url": "https://www.fashionnova.com/cdn/shop/products/01-10-22Studio4_ME_RL_13-58-44_34_F121870N_LightBlueWash_15692_KL.jpg?v=1641923689",
        "price": 19.99,
        "stock_quantity": 23,
        "category": "women's clothes"
    },
    {
        "name": "Petite Crossover Straight Leg Jeans - Medium Wash",
        "description": "Introducing the Petite Crossover Straight Leg Jeans in Medium Wash, also available in Light Wash. These jeans feature a unique crossover waistband and a classic 5-pocket design. Designed for all heights, they come in Petite, Regular, and Tall (35 lengths. With an 11.5 inch high rise and crafted from 100% non-stretch cotton, they offer a comfortable, vintage-inspired fit. Each pair is uniquely crafted through a specialized wash process. Perfect for any casual wardrobe.",
        "image_url": "https://www.fashionnova.com/cdn/shop/products/07-05-22Studio1_CE_MR_10-47-10_13_ZDJ1047P_MediumWash_6338_EH_468x@2x.jpg?v=1657232331",
        "price": 34.99,
        "stock_quantity": 23,
        "category": "women's clothes"
    },
    {
        "name": "Elegance in Motion: Casual Two-Piece Shorts Set",
        "description": "Elevate your style with the Elegance in Motion Two-Piece Shorts Set. Featuring a surplice neck short sleeve top and skinny lace-up elastic waist shorts, this solid color outfit offers comfort and sophistication. Perfect for casual outings, it provides a flattering silhouette with a chic, versatile look.",
        "image_url": "https://img.kwcdn.com/product/fancy/604383c3-9778-48c0-9f94-cf316e98915f.jpg?imageView2/2/w/800/q/70/format/webp",
        "price": 26.99,
        "stock_quantity": 18,
        "category": "women's clothes"
    },
    {
        "name": "Seaside Elegance: Chiffon Holiday Dress",
        "description": "Step into summer with the Seaside Elegance Chiffon Holiday Dress. This fashionable, casual, and elegant dress features a vibrant print, perfect for beach holidays. Designed for comfort and style, it's a must-have for your European and American vacations.",
        "image_url": "https://img.kwcdn.com/product/fancy/4d7b8aa8-f942-492e-95a1-aa4e11806577.jpg?imageView2/2/w/800/q/70/format/webp",
        "price": 19.99,
        "stock_quantity": 14,
        "category": "women's clothes"
    },
    {
        "name": "Kiana Tropical Maxi Dress - Black/Combo",
        "description": "Embrace tropical elegance with the Kiana Tropical Maxi Dress in Black/Combo. This sleeveless maxi dress features adjustable spaghetti straps, a flattering V-neck, and a tie-back detail. The elastic waist and faux button front add a touch of sophistication, while the front slit and ruffle trim enhance its feminine charm. Fully lined and made from 100% polyester, this non-stretch dress ensures comfort and style. Dress length is 59 inches. Note: Print placement may vary. Perfect for making a statement at any summer event.",
        "image_url": "https://www.fashionnova.com/cdn/shop/products/KianaTropicalMaxiDress-Blackcombo_MER_468x@2x.jpg?v=1652833141",
        "price": 44.99,
        "stock_quantity": 15,
        "category": "women's clothes"
    },
    {
        "name": "Sassy Straight Leg Jeans - Light Blue Wash",
        "description": "Step out in style with the Sassy Straight Leg Jeans in Light Blue Wash. These jeans feature a classic 5-pocket design, distressed detailing, and a 12\" ultra high rise for a flattering fit. With a 33\" inseam and crafted from 100% non-stretch cotton, they offer both comfort and durability. Each pair is unique due to the specialized wash and distressing process. Perfect for a chic, casual look.",
        "image_url": "https://www.fashionnova.com/cdn/shop/products/02-14-22Studio5_DD_AC_13-47-36_45_A1313_LightBlueWash_43262_KL.jpg?v=1644969899",
        "price": 39.99,
        "stock_quantity": 18,
        "category": "women's clothes"
    },
    {
        "name": "Graphic Red Lips Graphic Tee",
        "description": "Graphic Red Lips Graphic Tee",
        "image_url": "https://e2gworld.com/cdn/shop/files/20547828_4bdaad87-38cd-49a0-a893-e60fe31daf4a_596x798.jpg?v=1700663850",
        "price": 34.99,
        "stock_quantity": 12,
        "category": "women's clothes"
    },
    {
        "name": "Skinny Butt Lift Ripped Jeans",
        "description": "If you're looking for a pair of jeans that will enhance your figure and keep you stylish at the same time, then Skinny Butt Lift Ripped Jeans are the perfect choice for you. Made from premium quality cotton, these jeans are both comfortable and durable, ensuring that you'll be able to wear them time and time again. The high waist design of these jeans provides a flattering and slimming effect, while the skinny fit hugs your curves and accentuates your natural curves.",
        "image_url": "https://forwomenusa.com/cdn/shop/products/skinny-butt-lift-ripped-jeans-women-jeans-blue-s-china-forwomenusa-38583452664032.jpg?v=1675215831",
        "price": 47.89,
        "stock_quantity": 63,
        "category": "women's clothes"
    },
    {
        "name": "Just For You Ripped Non Stretch Straight Leg Jean",
        "description": "Pop in this oversized denim jacket and be ready to go. With it's classic medium wash, figure hugging waist and oversized chest fabric for a layered look. Pair with a cute dress or rock with your everyday jeans",
        "image_url": "https://www.fashionnova.com/cdn/shop/products/03-02-23Studio1_TH_B_10-32-03_27_FN24598FT36_LightWash_5871_EH.jpg?v=1678224286",
        "price": 27.99,
        "stock_quantity": 40,
        "category": "women's clothes"
    },
    {
        "name": "Casual Friday Set",
        "description": "Paired to perfection, the Casual Friday Set offers an effortless, instant outfit. This stunning ensemble includes a slim, cropped tank with a button-up design, scoop neckline, smocked back, and tie-back straps, paired with high-rise, wide-leg trousers featuring side pockets, top pleating, and a zip fly with button closure. Adorned in a summer-ready striped print, this set is perfect for chic, casual wear all season long.",
        "image_url": "https://images.urbndata.com/is/image/FreePeople/69701597_038_a/?$redesign-zoom-5x$",
        "price": 69.99,
        "stock_quantity": 13,
        "category": "women's clothes"
    },
    {
        "name": "Perri Linen Drop-Waist Mini",
        "description": "Forever romantic and versatile, the Perri Linen Drop-Waist Mini from our free-est collection is a true wear-everywhere staple. This sweet mini dress features a relaxed drop-waist silhouette, cap sleeves that can be worn off the shoulder, ruched detailing at the bust, button-up closures, and a tie detail at the back. Perfect for pairing with western boots for a fun look or with sandals and a swimsuit for a beachy vibe, this dress will be your go-to all season long.",
        "image_url": "https://images.urbndata.com/is/image/FreePeople/90111659_046_a/?$redesign-zoom-5x$",
        "price": 56.99,
        "stock_quantity": 23,
        "category": "women's clothes"
    },
    {
        "name": "We The Free Opal Swing Denim Jacket",
        "description": "Elevate your denim jacket collection with the We The Free Opal Swing Denim Jacket. This cool and unique jacket features dropped shoulders for a relaxed fit and defined pleating at the back, adding a special swingy touch. It comes with a button-front closure, double bust patch pockets, and a lower back hemline for a stylish and functional look. Perfect for layering and adding a trendy twist to any outfit.",
        "image_url": "https://images.urbndata.com/is/image/FreePeople/68349745_436_b/?$redesign-zoom-5x$",
        "price": 74.99,
        "stock_quantity": 26,
        "category": "women's clothes"
    },
    {
        "name": "We The Free Xena Slim Straight Jeans",
        "description": "So classic from our We The Free collection, the Xena Slim Straight Jeans feature a vintage high-rise fit with slim straight legs and 5-pocket styling. Made from authentic rigid cotton, these jeans offer a timeless look with a zip-fly and button closure, straight-leg style, and belt loops at the waistband. Perfect for any occasion, these jeans are the ideal wear-everywhere wardrobe staple.",
        "image_url": "https://images.urbndata.com/is/image/FreePeople/90291808_001_a/?$redesign-zoom-5x$",
        "price": 64.99,
        "stock_quantity": 15,
        "category": "women's clothes"
    },
    {
        "name": "Ring My Bells Bell Bottom Flare Jeans - Light Wash",
        "description": "Ring bae's bells, ring my bells bae! Shake things up in our classic Ring My Bell Bottoms! These jeans are perfect for any occasion or any season! If you don't grab the dark wash, be sure to grab the life wash!",
        "image_url": "https://shopswankaposh.com/cdn/shop/files/20231115-352A6927_2500x.jpg?v=1703022508",
        "price": 69.99,
        "stock_quantity": 30,
        "category": "women's clothes"
    },
    {
        "name": "Denim Pockets Wide Leg Cargo Overalls - Blue",
        "description": "Stay stylish and practical with our Denim Pockets Wide Leg Cargo Overalls in Blue. These regular silhouette overalls feature a boat neckline and a comfortable wide-leg design. Made from durable cotton fabric, they are both functional and fashionable, with multiple pockets for all your essentials. The sleeveless design and adjustable straps ensure a perfect fit, making these overalls an ideal choice for any casual outing.",
        "image_url": "https://img.staticdj.com/ff8dfaf54c0d2eca14c423c6db2e530a_750x.jpeg",
        "price": 64.99,
        "stock_quantity": 23,
        "category": "women's clothes"
    },
    {
        "name": "Cargo Pockets Straps Button Denim Romper Playsuit - Blue",
        "description": "Embrace casual chic with our Cargo Pockets Straps Button Denim Romper Playsuit in Blue. This stylish playsuit features cargo pocket decor, shoulder straps, and a buttoned waist for a flattering fit. Crafted from durable denim fabric, it offers both comfort and a trendy look. Perfect for everyday wear, this romper combines functionality with fashion, making it a versatile addition to your wardrobe.",
        "image_url": "https://img.staticdj.com/d5924a0bce78be3dc29650b8201f3b56_750x.jpeg",
        "price": 54.99,
        "stock_quantity": 29,
        "category": "women's clothes"
    },
    {
        "name": "For Your Thoughts High Rise Skinny Jeans - Medium Wash",
        "description": "Take a moment and gather your thoughts on these stylish jeans, featuring a high-rise waist. zippered closure, belt loops, front and rear pockets, and a skinny leg fit with distressing at the knees and frayed ankles.",
        "image_url": "https://shopswankaposh.com/cdn/shop/files/20240308-352A3971_2048x.jpg?v=1709915992",
        "price": 59.99,
        "stock_quantity": 15,
        "category": "women's clothes"
    },
    {
        "name": "Denim Strapless Splash Ink Print Cargo Jumpsuit",
        "description": "Make a bold statement with our Denim Strapless Splash Ink Print Cargo Jumpsuit. This eye-catching piece features a strapless design and a button-up closure, offering a sleek and modern look. The straight leg cut and multi-pocket details provide both style and functionality. Adorned with a unique splash ink print, this denim jumpsuit is perfect for those who love to stand out. Ideal for casual outings or trendy events, it's a must-have addition to your fashion-forward wardrobe.",
        "image_url": "https://img.staticdj.com/0036f882f88a142541ee87719d29bc7a_1080x.jpg",
        "price": 79.99,
        "stock_quantity": 12,
        "category": "women's clothes"
    },
    {
        "name": "Juniors' SO® BOHO Cardigan",
        "description": "Wrap yourself in cozy vibes with this super soft BOHO cardigan from SO.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6307158_Tan_Fairisle?wid=805&hei=805&op_sharpen=1",
        "price": 34.99,
        "stock_quantity": 20,
        "category": "teen's clothes"
    },
    {
        "name": "Juniors' SO® Two-Way Zipper Hooded Cardigan Sweater",
        "description": "You'll simply love the modern look of this juniors' hooded cardigan with a nifty two-way zipper.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6116544_Black?wid=805&hei=805&op_sharpen=1",
        "price": 31.99,
        "stock_quantity": 15,
        "category": "teen's clothes"
    },
    {
        "name": "Juniors' SO® Long Sleeve Ribbed Square Neck Top",
        "description": "Take your casual wardrobe to the next level with this long sleeve ribbed square neck juniors' cropped top from SO.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/5738968_Modern_White?wid=805&hei=805&op_sharpen=1",
        "price": 21.99,
        "stock_quantity": 25,
        "category": "teen's clothes"
    },
    {
        "name": "Boys 8-20 Sonoma Goods For Life® Everyday Raglan Tee in Regular & Husky",
        "description": "Casual comfort and style are effortless with this kids' everyday raglan tee from Sonoma Goods For Life.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/5593806_ALT4?wid=1500&hei=1500&op_sharpen=1&qlt=60",
        "price": 9.99,
        "stock_quantity": 15,
        "category": "teen's clothes"
    },
    {
        "name": "Kids 8-20 Nike Club Fleece Hoodie",
        "description": "Say hello to this Club Fleece Hoodie from Nike, an essential for running, jumping and laughing your way through the year.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6120527_Black?wid=805&hei=805&op_sharpen=1",
        "price": 49.99,
        "stock_quantity": 20,
        "category": "teen's clothes"
    },
    {
        "name": "Boys 8-20 Teenage Mutant Ninja Turtles Defenders Inc. Graphic Tee",
        "description": "Give his wardrobe a radical refresh with this boys' Ninja Turtles graphic tee.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/6450693?wid=805&hei=805&op_sharpen=1",
        "price": 14.99,
        "stock_quantity": 50,
        "category": "teen's clothes"
    },
    {
        "name": "Boys 10-16 OppoSuits Groovy Grey Solid Suit",
        "description": "When he looks good, he feels good, and that's exactly what will happen when your little dude wears this timeless suit. This OppoSuits grey ensemble is both stylish and comfortable, so he'll have the perfect outfit option for any special occasion.",
        "image_url": "https://media.kohlsimg.com/is/image/kohls/3911337?wid=805&hei=805&op_sharpen=1",
        "price": 79.99,
        "stock_quantity": 40,
        "category": "teen's clothes"
    },
    {
        "name": "Corvette Striped Mechanic Shirt",
        "description": "A classic mechanic-inspired style accented with authentic Corvette patches.",
        "image_url": "https://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dwc96d7690/62371010_102_main.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg",
        "price": 19.99,
        "stock_quantity": 50,
        "category": "teen's clothes"
    },
    {
        "name": "Solid High-Neck Ribbed Midi Dress",
        "description": "Wherever you go, you're making an entrance in this sleek, stretchy dress. Throw it on with a cute jacket and some casual kicks.",
        "image_url": "https://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dwd6baeccc/81251513_195_alt2.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg",
        "price": 22.99,
        "stock_quantity": 60,
        "category": "teen's clothes"
    },
    {
        "name": "Essentials Full-Zip Hoodie",
        "description": "The most relaxed, laid-back hoodie in your wardrobe. Get extra cozy and snag our matching joggers, too.",
        "image_url": "https://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dw2e34693b/81994430_223_alt1.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg",
        "price": 29.99,
        "stock_quantity": 80,
        "category": "teen's clothes"
    },
    {
        "name": "Relaxed Cargo Jean",
        "description": "A relaxed pair with your most-loved detail: cargo pockets. Fabric features recycled cotton, which is crafted from a mix of pre-and post-consumer waste to help reduce landfills.",
        "image_url": "https://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dw336bef52/64193761_176_alt1.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg",
        "price": 34.99,
        "stock_quantity": 13,
        "category": "teen's clothes"
    },
    {
        "name": "Airwalk French Terry Graphic Joggers",
        "description": "This French terry pair of joggers features an 'Airwalk' leg graphic, contrasting drawstring at the waist, on-seam side pockets, and elasticized trim.",
        "image_url": "https://www.forever21.com/dw/image/v2/BFKH_PRD/on/demandware.static/-/Sites-f21-master-catalog/default/dw8329a353/1_front_750/00462624-01.jpg?sw=1000&sh=1500",
        "price": 15.99,
        "stock_quantity": 96,
        "category": "teen's clothes"
    },
    {
        "name": "Aero Circle Pullover Hoodie",
        "description": "A seriously comfy hoodie for everyday lounging. Looks perfect with our matching sweats!",
        "image_url": "https://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dwc057d727/81063331_268_alt1.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg",
        "price": 14.99,
        "stock_quantity": 50,
        "category": "teen's clothes"
    },
    {
        "name": "OAKLAND VARSITY PRINTED OVERSIZED SWEATER",
        "description": "Sitting pretty at the top of our wishlist, reach comfort heaven this season in this sweatshirt from our latest collection...",
        "image_url": "https://media.boohoo.com/i/boohoo/fzz36832_ecru_xl/female-ecru-oakland-varsity-printed-oversized-sweater?w=450&qlt=default&fmt.jp2.qlt=70&fmt=auto&sm=fit",
        "price": 24.99,
        "stock_quantity": 23,
        "category": "teen's clothes"
    },
    {
        "name": "Drippin Hoodie - Black/combo",
        "description": "Model Height: 6'2 - Wearing Large. Big & Tall: Height 6'3- Wearing XXXL...",
        "image_url": "https://www.fashionnova.com/cdn/shop/products/DrippinHoodie-Blackcombo_MER_468x.jpg?v=1618955451",
        "price": 12.99,
        "stock_quantity": 40,
        "category": "teen's clothes"
    },
    {
        "name": "Mini Teenage Mutant Ninja Turtle Set - Black",
        "description": "Available In Black. Screen Tee Long Sleeve Short Set Teenage Mutant Ninja Turtle Graphic Tee",
        "image_url": "https://www.fashionnova.com/cdn/shop/files/01-02-24_S6_38_NJSBAQ5_Black_RA_AA_13-54-21_69285_PXF_468x.jpg?v=1705437028",
        "price": 24.99,
        "stock_quantity": 60,
        "category": "teen's clothes"
    },
    {
        "name": "Jacquard-knit Cotton Sweater",
        "description": "Jacquard-knit sweater in soft cotton. Long sleeves and ribbing at neck, cuffs, and hem.",
        "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F0a%2F41%2F0a41edf3e667dc4613073a0e5e80ec00f6cc9145.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BLOOKBOOK%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url[file:/product/main]",
        "price": 6.99,
        "stock_quantity": 50,
        "category": "kids clothes"
    },
    {
        "name": "Super Soft Skinny Fit Jeans",
        "description": "Jeans in flexible, supersoft, superstretch denim for added freedom of movement. Skinny fit through hip, thigh, and leg. Adjustable, elasticized waistband, zip fly with snap fastener, front pockets, and open back pockets.",
        "image_url": "https://lp2.hm.com/hmgoepprod?set=format%5Bwebp%5D%2Cquality%5B79%5D%2Csource%5B%2F2e%2F61%2F2e61f1567578a528c6a24a98caac0d7e5202dc74.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BLOOKBOOK%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url%5Bfile%3A%2Fproduct%2Fmain%5D",
        "price": 19.99,
        "stock_quantity": 60,
        "category": "kids clothes"
    },
    {
        "name": "Splash Ink UNSPEAKABLE Letter Print Boys Casual Pullover Hooded Long Sleeve Sweatshirt",
        "description": "Splash Ink UNSPEAKABLE Letter Print Boys Casual Pullover Hooded Long Sleeve Sweatshirt For Spring Fall, Kids Hoodie Tops Outdoor",
        "image_url": "https://img.kwcdn.com/thumbnail/s/258f6c87f52415c8da3aa532e4572dcf_020718fb5238.jpg?imageView2/2/w/800/q/70",
        "price": 12.99,
        "stock_quantity": 40,
        "category": "kids clothes"
    },
    {
        "name": "COLOR BLOCK POLAR SHERPA JACKET",
        "description": "Stay warm and stylish this winter with the Color Block Polar Sherpa Jacket. This super soft polar fleece piece is perfect for keeping cosy in the cold weather...",
        "image_url": "https://www.tinycottons.com/media/catalog/product/a/w/aw23-229-m42_6.jpg?quality=90&bg-color=255,255,255&fit=bounds&height=1920&width=1280&canvas=1280:1920",
        "price": 59.99,
        "stock_quantity": 26,
        "category": "kids clothes"
    },
    {
        "name": "STRIPES BODY",
        "description": "A cotton is a natural fiber which is sustainable, renewable and biodegradable. Pima is in the top one percent of cotton produced in the world. Twice as strong than regular cotton, it is trusted for its integrity and durability so its use results in longer-lasting products. Also, the farming practices employed comply with environmental and ethical...",
        "image_url": "https://www.tinycottons.com/media/catalog/product/a/w/aw23-058-m30_5.jpg?quality=90&bg-color=255,255,255&fit=bounds&height=1920&width=1280&canvas=1280:1920",
        "price": 24.99,
        "stock_quantity": 23,
        "category": "kids clothes"
    },
    {
        "name": "Wild Short Sleeve Kids Tee",
        "description": "Make your kid the wildest in the pack with this super soft tee! Perfect for any adventure, whether it's exploring the backyard or fighting off dragons. Make your little one look fierce and cool in this rad 'Wild' tee!",
        "image_url": "https://rags.com/cdn/shop/files/K01B4843.jpg?v=1698172624&width=1400",
        "price": 32.99,
        "stock_quantity": 50,
        "category": "kids clothes"
    },
    {
        "name": "Camel Check Short Sleeve Kids Essentials Tee",
        "description": "This super soft kids tee is ready to tackle playtime and look rad at the same time! Our kid’s tee in 'Camel Check' looks awesome for a day out. It's the total package for every trendy kid.",
        "image_url": "https://rags.com/cdn/shop/files/K01B6897.jpg?v=1699481144&width=1400",
        "price": 19.99,
        "stock_quantity": 40,
        "category": "kids clothes"
    },
    {
        "name": "Phantom Essentials Short Sleeve Chest Pocket Rounded Kids Tee",
        "description": "The softness and bold colors kids crave and the durability parents love!...",
        "image_url": "https://rags.com/cdn/shop/files/K01B3577.jpg?v=1702401241&width=1400",
        "price": 19.99,
        "stock_quantity": 40,
        "category": "kids clothes"
    },
    {
        "name": "Pink Check Essentials Short Sleeve Rounded Kids Tee",
        "description": "Show off your kid's cool style with our Essentials Kids Tee in Pink Checker...",
        "image_url": "https://rags.com/cdn/shop/files/K01B4308_4757c24d-7186-4a41-844f-18abc922c2ae.jpg?v=1698080122&width=1400",
        "price": 19.99,
        "stock_quantity": 50,
        "category": "kids clothes"
    },
    {
        "name": "Sagebrush Stripe Essentials Long Sleeve Pocket Kids Tee",
        "description": "The softness your kids crave at a price your wallet will appreciate. Part of our #1 best-selling collection...",
        "image_url": "https://rags.com/cdn/shop/files/K01B7308_78a8696d-56bc-4f56-b9a3-b928f19f90c3.jpg?v=1697821015&width=1400",
        "price": 21.99,
        "stock_quantity": 40,
        "category": "kids clothes"
    },
    {
        "name": "Checks & Hearts Short Sleeve Swing Dress",
        "description": "Get ready for some sweet style this Valentine's Day with our Short Sleeve Swing Dress!...",
        "image_url": "https://rags.com/cdn/shop/files/K01B9944_92eba006-82ce-41cc-b9a0-26e9a6cc3265.jpg?v=1705197805&width=1400",
        "price": 42.99,
        "stock_quantity": 25,
        "category": "kids clothes"
    },
    {
        "name": "Rose Pink Essentials Short Sleeve with Chest Pocket Dress",
        "description": "Unconventional dressing starts with a whole new fit! The Essentials Short Sleeve Dress brings the fun and goes the distance...",
        "image_url": "https://rags.com/cdn/shop/files/K01B3101.jpg?v=1692900157&width=1400",
        "price": 29.99,
        "stock_quantity": 35,
        "category": "kids clothes"
    },
    {
        "name": "Camel Kids Essentials Joggers",
        "description": "Stylish, durable, and versatile. The perfect amount of stretch and comfort will make these your kiddo's new favorite joggers...",
        "image_url": "https://rags.com/cdn/shop/files/INFANTJOGGERS.png?v=1690391231&width=1400",
        "price": 34.99,
        "stock_quantity": 34,
        "category": "kids clothes"
    },
    {
        "name": "Brick Red Essentials 3/4 Rolled Sleeve Henley Long Rag Romper",
        "description": "Part of our #1 best-selling collection, Essentials Rags are your kid's new favorite basics!...",
        "image_url": "https://rags.com/cdn/shop/files/K01B1748.jpg?v=1696980875&width=1400",
        "price": 24.99,
        "stock_quantity": 25,
        "category": "kids clothes"
    },
    {
        "name": "Newborn Rag in Phantom Newborn Essentials Peekabooty™ Rag Romper Long Sleeve",
        "description": "Ahhh, the newborn stage: Full of dozens of diaper and outfit changes. We're here to make life easier for you in those first few months...",
        "image_url": "https://rags.com/cdn/shop/products/4_1425007b-83a7-4fa8-b567-c830b6148fd6.jpg?v=1695913454&width=1400",
        "price": 25.99,
        "stock_quantity": 25,
        "category": "kids clothes"
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


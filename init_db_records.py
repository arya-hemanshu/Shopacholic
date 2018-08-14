import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Shopacholic import database, application
from Shopacholic.models.product_type import ProductType
from Shopacholic.models.product import Product

# Creating initial product types
books = ProductType(type_name = 'Books')
database.session.add(books)
database.session.flush()

# Creating initial products for books
sf_engineering = Product(books, 'Software Engineering', 'sf_engineering', 
                        'The Fundamental Practice of Software Engineering', 
                        'Software Engineering introduces students to the overwhelmingly \
                        important subject of software programming and development. In the \
                        past few years, computer systems have come to dominate not just our \
                        technological growth, but the foundations of our world’s major \
                        industries. This text seeks to lay out the fundamental concepts \
                        of this huge and continually growing subject area in a clear and \
                        comprehensive manner.', 43)

clean_architecture = Product(books, 'Clean Architecture', 'clean_architecture',
                            'Clean Architecture is essential reading for every \
                            software architect, systems analyst, system designer, \
                            and software manager', 'As with his other books, Martins \
                            Clean Architecture doesnt merely present multiple \
                            choices and options, and say "use your best judgment": \
                            it tells you what choices to make, and why those choices are \
                            critical to your success', 20)

b_sf_engineering = Product(books, 'Begininning Software Engineering', 'b_sf_engineering', 
                            'A complete introduction to building robust and reliable software', 
                            'Beginning Software Engineering demystifies the software engineering \
                            methodologies and techniques that professional developers use to design \
                            and build robust, efficient, and consistently reliable software. Free of \
                            jargon and assuming no previous programming, development, or management \
                            experience, this accessible guide explains important concepts and \
                            techniques that can be applied to any programming language.', 27)

clean_code = Product(books, 'Clean Code', 'clean_code', 
                    'A Handbook of Agile Software Craftsmanship',
                    'Even bad code can function. But if code isn’t clean, it can bring a development \
                    organization to its knees. Every year, countless hours and significant resources \
                    are lost because of poorly written code. But it doesn’t have to be that way. Noted \
                    software expert Robert C. Martin presents a revolutionary paradigm with Clean Code: \
                    A Handbook of Agile Software Craftsmanship . Martin has teamed up with his colleagues \
                    from Object Mentor to distill their best agile practice of cleaning code “on the fly” \
                    into a book that will instill within you the values of a software craftsman and make \
                    you a better programmer—but only if you work at it.', 22)

intro_to_algorithms = Product(books, 'Introduction to Algorithms', 'intro_to_algo', 
                                'This is the definitive textbook on algorithms, and something no Computer \
                                Science student or researcher should ever be without.',
                                'A new edition of the essential text and professional reference, with \
                                substantial new material on such topics as vEB trees, multithreaded \
                                algorithms, dynamic programming, and edge-based flow.Some books on \
                                algorithms are rigorous but incomplete; others cover masses of \
                                material but lack rigor. Introduction to Algorithms uniquely combines \
                                rigor and comprehensiveness. The book covers a broad range of algorithms \
                                in depth, yet makes their design and analysis accessible to all levels \
                                of readers. Each chapter is relatively self-contained and can be used \
                                as a unit of study.', 62)


database.session.add(sf_engineering)
database.session.add(clean_architecture)
database.session.add(b_sf_engineering)
database.session.add(clean_code)
database.session.add(intro_to_algorithms)
database.session.commit()

monitors = ProductType(type_name = 'Monitors')
database.session.add(monitors)
database.session.flush()

# Creating initial product for monitors
dell = Product(monitors, 'Dell UltraSharp', 'dell', 
                'Dell UltraSharp U2415 24 Inch IPS 1920x1200 (16:10) 860-BBEY',
                'Superior performance: Colour accuracy shines through in vivid detail over a \
                high-performance, spacious display. More ways to connect: Charge, connect \
                and project handheld devices and more with extensive ports. Reliable and \
                eco-efficient: Count on the Dell Premium Panel Guarantee and an \
                environmentally conscious design', 226)

acer = Product(monitors, 'Acer K222HQL', 'acer', 
                'Acer K222HQL 21.5-inch Full HD Monitor (TN panel, 5ms, HDMI, DVI) - Black',
                'The Acer K222HQLbid Monitor is suitable for today’s work intensive business \
                environments and everyday PC use. Efficient and cost-effective, the Acer \
                K222HQLbid Monitor offers smart design, ease-of-use and image quality that \
                minimises fatigue and maximises productivity.', 84)

alienware = Product(monitors, 'Alienware AW2518H', 'alienware', 
                    'Alienware AW2518H 24.5 Inch TN Gaming Monitor (Black Grey) \
                    (1 ms Response Time, Full HD 1920 x 1080 at 240 Hz, NVidia G-Sync, \
                    DP/HDMI, USB, Alienware FX Lighting)', 'Introducing all-new Alienware \
                    monitors, mice and keyboards featuring the iconic design you trust for \
                    exhilarating, immersive gaming. Whether you are just starting your \
                    collection, or rounding out your arsenal, Alienware accessories are \
                    built to enhance your gaming experience as you journey deeper \
                    into the game.', 460)

asus = Product(monitors, 'ASUS MB169B', 'asus', 
                'ASUS MB169B+ 15.6" Portable USB Monitor, FHD (1920x1080), IPS',
                'The 15.6-inch MB169B+ portable USB-powered monitor needs just one USB cable \
                for both its video signal and power to deliver up to a Full HD resolution. \
                Thanks to the higher bandwidth of USB 3.0, experience fast, fluid images \
                from your connected device that makes having an on-the-go multi-display \
                setup a reality.', 186)

benq = Product(monitors, 'BenQ EW2775ZH', 'benq', 
                'BenQ EW2775ZH 27 Inch Eye-Care Monitor, 1920 x 1080 FHD, Brightness \
                Intelligence Sensor, 3000:1 Native Contrast Ratio, Low Blue Light Plus, \
                Flicker-Free, Black', 'Watching your favourite videos or movies should be easy \
                on your eyes. Brightness Intelligence Technology (B.I Tech) optimises display \
                performance for videos and movies by automatically adjusting to ambient light \
                and on-screen content, protecting your eyes while delivering premium image quality. \
                So sit back, relax and soak up your favourite videos', 168)


database.session.add(dell)
database.session.add(acer)
database.session.add(alienware)
database.session.add(asus)
database.session.add(benq)

database.session.commit()


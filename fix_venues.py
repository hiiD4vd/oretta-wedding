import os
import random
import re

base_dir = r'd:\daud\projek bisnis\oretta wedding'
index_path = os.path.join(base_dir, 'index.html')
venue_path = os.path.join(base_dir, 'venue.html')

images = [
    'wa_weddingplanner_604594719_18378691975153361_8482502786223473575_n.jpg',
    'wa_weddingplanner_623657218_18382768870153361_5163603875966347756_n.jpg',
    'wa_weddingplanner_624595716_18383020762153361_8584612868500801603_n.jpg',
    'wa_weddingplanner_626624517_18384099499153361_494313317223290399_n.jpg',
    'wa_weddingplanner_639514205_18386872477153361_6399780977498644749_n.jpg',
    'wa_weddingplanner_639797907_18387199210153361_2066491183921168205_n.jpg',
    'wa_weddingplanner_639847445_18387637324153361_8944207428109375048_n.jpg',
    'wa_weddingplanner_641330447_18387860746153361_2362668870059087128_n.jpg',
    'wa_weddingplanner_645509220_18388809946153361_9164901203461665803_n.jpg',
    'wa_weddingplanner_648997738_18388724632153361_8234042692745380489_n.jpg',
    'wa_weddingplanner_649964684_18389205679153361_8706861645018206310_n.jpg',
    'wa_weddingplanner_669655868_18394381462153361_2378700212379607255_n.jpg',
    'wa_weddingplanner_670763662_18395960650153361_7224281693566297419_n.jpg',
    'wa_weddingplanner_670767868_18395230966153361_7737434759031360775_n.jpg',
    'wa_weddingplanner_671754614_18396062122153361_3443275959358492930_n.jpg'
]

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace portfolio_X.png with random real image
    def replace_portfolio(match):
        return f'/images/{random.choice(images)}'
        
    content = re.sub(r'/images/portfolio_[1-6]\.png', replace_portfolio, content)
    
    # Fix the height: 200px to aspect-ratio: 4/5; height: auto;
    content = content.replace('height: 200px;', 'aspect-ratio: 4/5; height: auto;')
    
    # Fix object-fit: cover; to also have object-position: center 25%;
    content = content.replace('object-fit: cover;"', 'object-fit: cover; object-position: center 25%;"')
    
    # Make sure we don't accidentally duplicate object-position if run multiple times
    content = content.replace('object-position: center 25%; object-position: center 25%;', 'object-position: center 25%;')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Processed {path}')

process_file(index_path)
process_file(venue_path)
print('Done!')

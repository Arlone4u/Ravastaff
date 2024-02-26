import os
import json
from jinja2 import Template

def generate_html(config_file, template_file, output_file):
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', config_file))

    template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates', template_file))

    try:
        with open(config_path, 'r') as cfg_file:
            config_data = json.load(cfg_file)
            
        home_data = config_data.get('HOME', {})
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output'))
    os.makedirs(output_folder, exist_ok=True)

    output_file_path = os.path.join(output_folder, output_file)

    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    template = Template(template_content)

    rendered_html = template.render(
        propertyAddress=home_data.get('propertyAddress', ''),
        images=home_data.get('images', {}),
        title=home_data.get('title', ''),
        menu=home_data.get('menu', []),
        openHouse=home_data.get('openHouse',[]),
        price=home_data.get('price', ''),
        extendedAddress=home_data.get('extendedAddress', ''),
        details=home_data.get('details', []),
        file=home_data.get('file', []),
        propertyDescription=home_data.get('propertyDescription', ''),
        featureTitle=home_data.get('featureTitle', ''),
        features=home_data.get('features', []),
        propertyVideos=home_data.get('propertyVideos', []),
        floorPlans=home_data.get('floorPlans', []),
        propertyRealtor=home_data.get('propertyRealtor', []),
        inquiry=home_data.get('inquiry', []),
        inquiryButtons=home_data.get('inquiryButtons', []),
        footerDetails=home_data.get('footerDetails', []),
        footerImage=home_data.get('footerImage', ''),
        icons=home_data.get('icons', []),
    )

    with open(output_file_path, 'w') as output_file:
        output_file.write(rendered_html)

    print(f"Generated HTML saved to: {output_file_path}")

if __name__ == "__main__":
    generate_html('syd_config.cfg', 'syd_dollar.html', 'syd_final.html')

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
        address=home_data.get('address', ''),
        images=home_data.get('images', {}),
        title=home_data.get('title', ''),
        menu=home_data.get('menu', []),
         houseviewing1=home_data.get('houseviewing1', ''),
        houseviewing2=home_data.get('houseviewing2', ''),
        day1=home_data.get('day1', ''),
        date1=home_data.get('date1', ''),
        time1=home_data.get('time1', ''),
         day2=home_data.get('day2', ''),
        date2=home_data.get('date2', ''),
        time2=home_data.get('time2', ''),
         day3=home_data.get('day3', ''),
        date3=home_data.get('date3', ''),
        time3=home_data.get('time3', ''),
        info=home_data.get('info', ''),
        price=home_data.get('price', ''),
        titleAddress=home_data.get('titleAddress', ''),
        extendedAddress=home_data.get('extendedAddress', ''),
        details=home_data.get('details', []),
        file=home_data.get('file', []),
        propertyDescription=home_data.get('propertyDescription', ''),
        featureTitle=home_data.get('featureTitle', ''),
        features=home_data.get('features', []),
        propertyVideos=home_data.get('propertyVideos', []),
        propertyRealtor=home_data.get('propertyRealtor', []),
        inquiry=home_data.get('inquiry', []),
        inquiryButtons=home_data.get('inquiryButtons', []),
        footerDetails=home_data.get('footerDetails', [])
    )

    with open(output_file_path, 'w') as output_file:
        output_file.write(rendered_html)

    print(f"Generated HTML saved to: {output_file_path}")

if __name__ == "__main__":
    generate_html('syd_config.cfg', 'syd_dollar.html', 'syd_final.html')

<?php
function generate_html($config_file, $template_file, $output_file) {
    // Get the absolute path to the config file
    $config_path = realpath(dirname(__FILE__) . '/../config/' . $config_file);

    // Get the absolute path to the template file
    $template_path = realpath(dirname(__FILE__) . '/../templates/' . $template_file);

    // Read the JSON configuration file
    $config_data = json_decode(file_get_contents($config_path), true);

    // Create the 'output' folder if it doesn't exist
    $output_folder = realpath(dirname(__FILE__) . '/../output');
    if (!file_exists($output_folder)) {
        mkdir($output_folder, 0755, true);
    }

    // Set the output file path inside the 'output' folder
    $output_file_path = $output_folder . '/' . $output_file;

    // Read the HTML template file
    $template_content = file_get_contents($template_path);

    // Substitute values from the configuration into the template
    // In PHP, you can directly use the extracted $config_data array
    ob_start();
    extract($config_data);
    include '../templates/' . $template_file;
    $rendered_html = ob_get_clean();

    // Save the rendered HTML to the output file
    file_put_contents($output_file_path, $rendered_html);

    // Display the generated HTML path in the console (optional)
    echo "Generated HTML saved to: $output_file_path\n";
}

// Usage
generate_html('syd.cfg', 'syd.html', 'syd.html');
?>

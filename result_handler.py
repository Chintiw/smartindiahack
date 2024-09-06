def save_results(results, output_file):
    with open(output_file, 'w') as f:
        for result in results:
            f.write(f"File: {result['filename']}\n")
            f.write(f"Classification: {result['classification']}\n")
            f.write(f"Extracted text: {result['text'][:100]}...\n\n")

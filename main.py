import os

from image_processor import extract_text_from_image
from word_list_handler import load_word_list
from content_classifier import classify_content
from file_handler import get_image_files
from result_handler import save_results

def process_image(image_path, dangerous_words):
    extracted_text = extract_text_from_image(image_path)
    classification = classify_content(extracted_text, dangerous_words)
    return classification, extracted_text

def process_folder(folder_path, word_list_path, output_file):
    dangerous_words = load_word_list(word_list_path)
    results = []

    for filename in get_image_files(folder_path):
        image_path = os.path.join(folder_path, filename)
        try:
            classification, text = process_image(image_path, dangerous_words)
            results.append({
                'filename': filename,
                'classification': classification,
                'text': text
            })
            print(f"Processed {filename}: {classification}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

    save_results(results, output_file)
    return results

if __name__ == "__main__":
    folder_path = '/home/chinu/SIH/sih2024/imgs'
    word_list_path = 'words.txt'
    output_file = 'results.txt'

    results = process_folder(folder_path, word_list_path, output_file)
    print(f"\nProcessing complete. Results saved to {output_file}")
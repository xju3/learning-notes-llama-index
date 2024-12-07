
from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import (DocxReader, 
                                      HWPReader, 
                                      PDFReader, 
                                      EpubReader, 
                                      FlatReader, 
                                      HTMLTagReader, 
                                      ImageCaptionReader, 
                                      ImageReader, 
                                      ImageVisionLLMReader, 
                                      IPYNBReader, 
                                      MarkdownReader, 
                                      MboxReader, 
                                      PptxReader, 
                                      PandasCSVReader, 
                                      PandasExcelReader,
                                      VideoAudioReader, 
                                      UnstructuredReader, 
                                      PyMuPDFReader, 
                                      ImageTabularChartReader, 
                                      XMLReader, 
                                      PagedCSVReader, 
                                      CSVReader, 
                                      RTFReader,)

def read_files_from_directory(dir):
    reader = SimpleDirectoryReader(dir)
    return reader.load_data()
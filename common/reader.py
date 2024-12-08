
import os
import nest_asyncio
from pathlib import Path
from io import BufferedIOBase
from typing import List, Union
from llama_index.core import SimpleDirectoryReader
from llama_parse import LlamaParse
from llama_index.readers.smart_pdf_loader import SmartPDFLoader
from llama_index.readers.pdf_marker import PDFMarkerReader
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

FileInput = Union[str, bytes, BufferedIOBase]

def pdf_marker_reader(file_name):
    reader = PDFMarkerReader()
    return reader.load_data(Path(file_name))

def smart_pdf_reader(file_name):
    '''
        online pdf file reader
    '''
    llmsherpa_api_url = "https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all"
    pdf_url = "https://arxiv.org/pdf/1910.13461.pdf"  # also allowed is a file path e.g. /home/downloads/xyz.pdf
    pdf_loader = SmartPDFLoader(llmsherpa_api_url=llmsherpa_api_url)
    return pdf_loader.load_data(pdf_url)

def read_files_from_directory(dir):
    reader = SimpleDirectoryReader(dir)
    return reader.load_data()

def read_files_by_llamaParse(file_input: Union[List[FileInput], FileInput]):
    nest_asyncio.apply()
    parses = LlamaParse(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY"),  # can also be set in your env as LLAMA_CLOUD_API_KEY
        result_type="markdown",  # "markdown" and "text" are available
        verbose=True,
    )
    return parses.load_data(file_input)

from pdfrw import PdfReader, PdfWriter, PageMerge
import config


class SignDocument:
    def __init__(self, stamp: str, input_name: str, output: str, folder: str):
        self.stamp_file = config.path_template + folder + '\\' + stamp
        self.input_file = config.path_template + folder + '\\' + input_name
        self.output_file = config.path_template + folder + '\\' + output
        self.reader_input = PdfReader(self.input_file)
        self.watermark_input = PdfReader(self.stamp_file)
        self.page_stamp = self.watermark_input.pages[0]
        self.writer_file = PdfWriter()

    def signed_file(self):
        for current_page in range(len(self.reader_input.pages)):
            merge_page = PageMerge(self.reader_input.pages[current_page])
            merge_page.add(self.page_stamp).render()

        # write the modified content to disk
        self.writer_file.write(self.output_file, self.reader_input)




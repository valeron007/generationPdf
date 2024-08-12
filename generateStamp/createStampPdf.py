from generateStamp import stamp as st


class CreateStampPdf:
    @staticmethod
    def createPdf(stamp, position, folder_name):
        width = 150
        height = 50
        stamp_pdf = st.StampGen(stamp.get_rand_name() + '.png',
                                stamp.get_rand_name() + "_stamp.pdf", width, height, position['x'], position['y'])
        stamp_pdf.generateStampForEmployee(folder_name)

    @staticmethod
    def create_brcode_pdf(image_code, template_pdf, position, width, height, folder_name):
        width = width
        height = height
        stamp_pdf = st.StampGen(image_code,
                                template_pdf, width, height, position['x'], position['y'])
        stamp_pdf.generateBRCodeForEmployee(folder_name)




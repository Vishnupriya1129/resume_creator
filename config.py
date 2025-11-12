import os

class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
    DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "generated_resumes")

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}

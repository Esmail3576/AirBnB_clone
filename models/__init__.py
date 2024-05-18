from models.engine.file_storage import FileStorage

global storage

storage = FileStorage()
storage.reload()
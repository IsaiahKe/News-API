class Article:
    '''
    initialize the class articles 
    '''
    def __init__(self,source,author,title,description,url,urltoimage,content,publishedat):
        self.source=source
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urltoimage=urltoimage
        self.content=content
        self.publishedat=publishedat

class Source:
    '''
    initialize the class source 
    '''
    def __init__(self,id,name,description,url,category,language,country):
        
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category
        self.language=language
        self.country=country
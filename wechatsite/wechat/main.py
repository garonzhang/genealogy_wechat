import os, os.path
import member_search 
import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
              <link href="/static/css/style.css" rel="stylesheet">
          </head>
          <body>
            <form method="get"  width=80% action="s_name">
              <input type="text" value="请输入姓名" name="keyword" style="width:180px;height:35px"/>
              <button style="width:80px;height:35px" type="submit">查询</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def s_name(self, keyword=""):
        content = member_search.search_by_keyword(keyword) 
        return content 

    @cherrypy.expose
    def s_id(self,member_id=1):
        content = member_search.get_tree(member_id) 
        return content 

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public/css'
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)



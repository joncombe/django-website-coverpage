from django.db import models


class WebsiteCoverPage(models.Model):
    DEFAULT_HTML = """<table onclick="websiteCoverPage.close()">
  <tr>
    <td>
      <img src="/path/to/image.png" />
    </td>
  </tr>
</table>"""

    DEFAULT_STYLE = """#websitecoverpage {
  background: rgba(0, 0, 0, 0.5);
  height: 100vh;
  left: 0;
  position: fixed;
  right: 0;
  top: 0;
  z-index: 9999998;
}

#websitecoverpage table, tr {
  height: 100vh;
  width: 100%;
}

#websitecoverpage td {
  padding: 25px;
  text-align: center;
  vertical-align: middle;
}

#websitecoverpage img {
  box-shadow: 0px 0px 25px 5px rgba(0, 0, 0, 0.5);
  cursor: pointer;
  max-width: 800px;
  width: 100%;
}"""

    name = models.CharField(max_length=255)
    html = models.TextField(blank=True, default=DEFAULT_HTML)
    style = models.TextField(blank=True, default=DEFAULT_STYLE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return self.name
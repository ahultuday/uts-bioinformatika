"""
Script sederhana untuk membuat template file XML untuk BEAST
"""

def generate_xml(output_file):
    content = """<beast>
  <run chainLength='1000000'>
    <!-- XML Generated Automatically -->
  </run>
</beast>"""
    with open(output_file, "w") as f:
        f.write(content)

if __name__ == "__main__":
    generate_xml("output.xml")

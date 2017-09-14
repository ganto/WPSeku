from distutils.core import setup

setup(name='wpseku',
      version='0.2.1',
      author='Momo Outaadl (M4all0k)',
      license='GPL-3',
      description='Black box WordPress vulnerability scanner',
      url='https://github.com/m4ll0k/WPSeku',
      packages=[
          'wpseku',
          'wpseku.data',
          'wpseku.lib',
          'wpseku.modules',
          'wpseku.modules.attack',
          'wpseku.modules.bruteforce',
          'wpseku.modules.discovery',
          'wpseku.modules.discovery.generic',
          'wpseku.modules.discovery.plugins',
          'wpseku.modules.discovery.themes',
          'wpseku.modules.discovery.users',
      ],
      package_dir={
          'wpseku.data': 'data',
          'wpseku.lib': 'lib',
          'wpseku.modules': 'modules',
      },
      package_data={
          'wpseku.data': [
              '*.txt',
          ],
      },
      scripts=[
          'bin/wpseku',
      ],
)

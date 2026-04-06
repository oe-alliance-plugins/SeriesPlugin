from setuptools import setup
import setup_translate

pkg = 'Extensions.SeriesPlugin'
setup(name='enigma2-plugin-extensions-seriesplugin',
       version='3.0',
       description='Find and rename series',
       package_dir={pkg: 'SeriesPlugin'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'Images/blue_round.png', 'Images/green_round.png', 'Images/minus.png', 'Images/plus.png', 'Images/red_round.png', 'Images/yellow_round.png', 'Logos/Wunschliste.png', 'Logos/Fernsehserien.png', 'maintainer.info', 'LICENSE', 'plugin.png', 'Skins/*.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )

from django.db import models
from django.core.urlresolvers import reverse

ETHNICITY = (
    ('American Indian / Alaskan Native', 'American Indian / Alaskan Native'),
    ('Asian / Pacific Islander', 'Asian / Pacific Islander'),
    ('Black,  non-Hispanic', 'Black,  non-Hispanic'),
    ('Hispanic', 'Hispanic'),
    ('White,  non-Hispanic', 'White,  non-Hispanic'),
    ('Unknown / declined to state', 'Unknown / declined to state'),
    ('International student', 'International student')
)

GENDER = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Not stated', 'Not stated')
)

MAJOR = (
    ('Arts | Art', 'Arts | Art'),
    ('Arts | Dance', 'Arts | Dance'),
    ('Arts | Drama', 'Arts | Drama'),
    ('Arts | Music - Performance', 'Arts | Music - Performance'),
    ('Arts | Music', 'Arts | Music'),
    ('Arts | Studio Art', 'Arts | Studio Art'),
    ('Arts | Undeclared', 'Arts | Undeclared'),
    ('Biological Sciences | Biological Sciences', 'Biological Sciences | Biological Sciences'),
    ('Biological Sciences | Biology/Education', 'Biological Sciences | Biology/Education'),
    ('Biological Sciences | Ecology and Evolutionary Biology', 'Biological Sciences | Ecology and Evolutionary Biology'),
    ('Business | Business Administration', 'Business | Business Administration'),
    ('Education | Education Sciences', 'Education | Education Sciences'),
    ('Education | Undeclared', 'Education | Undeclared'),
    ('Engineering | Aerospace Engineering', 'Engineering | Aerospace Engineering'),
    ('Engineering | Biomedical Engineering', 'Engineering | Biomedical Engineering'),
    ('Engineering | Biomedical Engineering: Premed', 'Engineering | Biomedical Engineering: Premed'),
    ('Engineering | Chemical Engineering', 'Engineering | Chemical Engineering'),
    ('Engineering | Civil Engineering', 'Engineering | Civil Engineering'),
    ('Engineering | Computer Engineering', 'Engineering | Computer Engineering'),
    ('Engineering | Computer Science and Engineering', 'Engineering | Computer Science and Engineering'),
    ('Engineering | Electrical Engineering', 'Engineering | Electrical Engineering'),
    ('Engineering | Environmental Engineering', 'Engineering | Environmental Engineering'),
    ('Engineering | Materials Science Engineering', 'Engineering | Materials Science Engineering'),
    ('Engineering | Mechanical Engineering', 'Engineering | Mechanical Engineering'),
    ('Engineering | Undeclared', 'Engineering | Undeclared'),
    ('Humanities | African-American Studies', 'Humanities | African-American Studies'),
    ('Humanities | Art History', 'Humanities | Art History'),
    ('Humanities | Asian American Studies', 'Humanities | Asian American Studies'),
    ('Humanities | Chinese Language and Literature', 'Humanities | Chinese Language and Literature'),
    ('Humanities | Chinese Studies', 'Humanities | Chinese Studies'),
    ('Humanities | Classical Civilization', 'Humanities | Classical Civilization'),
    ('Humanities | Classics', 'Humanities | Classics'),
    ('Humanities | Comparative Literature', 'Humanities | Comparative Literature'),
    ('Humanities | East Asian Cultures', 'Humanities | East Asian Cultures'),
    ('Humanities | English', 'Humanities | English'),
    ('Humanities | European Studies', 'Humanities | European Studies'),
    ('Humanities | Film and Media Studies', 'Humanities | Film and Media Studies'),
    ('Humanities | French', 'Humanities | French'),
    ('Humanities | Gender and Sexuality Studies', 'Humanities | Gender and Sexuality Studies'),
    ('Humanities | German Studies', 'Humanities | German Studies'),
    ('Humanities | Global Cultures', 'Humanities | Global Cultures'),
    ('Humanities | History', 'Humanities | History'),
    ('Humanities | Japanese Lanuage and Literature', 'Humanities | Japanese Lanuage and Literature'),
    ('Humanities | Korean Literature and Culture', 'Humanities | Korean Literature and Culture'),
    ('Humanities | Latin', 'Humanities | Latin'),
    ('Humanities | Literary Journalism', 'Humanities | Literary Journalism'),
    ('Humanities | Philosophy', 'Humanities | Philosophy'),
    ('Humanities | Religious Studies', 'Humanities | Religious Studies'),
    ('Humanities | Spanish', 'Humanities | Spanish'),
    ('Humanities | Undeclared', 'Humanities | Undeclared'),
    ('Info and Computer Sci | Biomedical Computing', 'ICS | Biomedical Computing'),
    ('Info and Computer Sci | Business Information Management', 'ICS | Business Information Management'),
    ('Info and Computer Sci | Computer Game Science', 'ICS | Computer Game Science'),
    ('Info and Computer Sci | Computer Science', 'ICS | Computer Science'),
    ('Info and Computer Sci | Computer Science and Engineering', 'ICS | Computer Science and Engineering'),
    ('Info and Computer Sci | Data Science', 'ICS | Data Science'),
    ('Info and Computer Sci | Informatics', 'ICS | Informatics'),
    ('Info and Computer Sci | Information and Computer Science', 'ICS | Information and Computer Science'),
    ('Info and Computer Sci | Software Engineering', 'ICS | Software Engineering'),
    ('Info and Computer Sci | Undeclared', 'ICS | Undeclared'),
    ('Nursing Science | Nursing Science', 'Nursing Science | Nursing Science'),
    ('Pharmaceutical Sciences | Pharmaceutical Sciences', 'Pharmaceutical Sciences | Pharmaceutical Sciences'),
    ('Physical Sciences | Applied Physics', 'Physical Sciences | Applied Physics'),
    ('Physical Sciences | Chemistry', 'Physical Sciences | Chemistry'),
    ('Physical Sciences | Earth and Environmental Sciences', 'Physical Sciences | Earth and Environmental Sciences'),
    ('Physical Sciences | Earth and Environmental Studies', 'Physical Sciences | Earth and Environmental Studies'),
    ('Physical Sciences | Earth System Science', 'Physical Sciences | Earth System Science'),
    ('Physical Sciences | Environmental Science', 'Physical Sciences | Environmental Science'),
    ('Physical Sciences | Mathematics', 'Physical Sciences | Mathematics'),
    ('Physical Sciences | Physics', 'Physical Sciences | Physics'),
    ('Physical Sciences | Undeclared', 'Physical Sciences | Undeclared'),
    ('Public Health | Public Health Policy', 'Public Health | Public Health Policy'),
    ('Public Health | Public Health Sciences', 'Public Health | Public Health Sciences'),
    ('Social Ecology | Criminology, Law and Society', 'Social Ecology | Criminology, Law and Society'),
    ('Social Ecology | Psychology and Social Behavior', 'Social Ecology | Psychology and Social Behavior'),
    ('Social Ecology | Social Ecology', 'Social Ecology | Social Ecology'),
    ('Social Ecology | Undeclared', 'Social Ecology | Undeclared'),
    ('Social Ecology | Urban Studies', 'Social Ecology | Urban Studies'),
    ('Social Sciences | Anthropology', 'Social Sciences | Anthropology'),
    ('Social Sciences | Business Economics', 'Social Sciences | Business Economics'),
    ('Social Sciences | Chicano/Latino Studies', 'Social Sciences | Chicano/Latino Studies'),
    ('Social Sciences | Cognitive Sciences', 'Social Sciences | Cognitive Sciences'),
    ('Social Sciences | Economics', 'Social Sciences | Economics'),
    ('Social Sciences | International Studies', 'Social Sciences | International Studies'),
    ('Social Sciences | Linguistics', 'Social Sciences | Linguistics'),
    ('Social Sciences | Political Science', 'Social Sciences | Political Science'),
    ('Social Sciences | Psychology ', 'Social Sciences | Psychology '),
    ('Social Sciences | Quantitative Economics', 'Social Sciences | Quantitative Economics'),
    ('Social Sciences | Social Policy and Public Service', 'Social Sciences | Social Policy and Public Service'),
    ('Social Sciences | Social Science', 'Social Sciences | Social Science'),
    ('Social Sciences | Sociology', 'Social Sciences | Sociology'),
    ('Social Sciences | Undeclared', 'Social Sciences | Undeclared'),
    ('Undergrad Education | Undeclared', 'Undergrad Education | Undeclared')
)

RESIDENCY = (
    ('California resident', 'California resident'),
    ('Other U.S. citizens or permanent residents', 'Other U.S. citizens or permanent residents'),
    ('International students', 'International students')
)
HIGH_SCHOOL = (
    ('OTHER / NOT LISTED', 'OTHER / NOT LISTED'),
    ('ABRAHAM LINCOLN SR HIGH SCHOOL', 'ABRAHAM LINCOLN SR HIGH SCHOOL'),
    ('ALAMEDA HIGH SCHOOL', 'ALAMEDA HIGH SCHOOL'),
    ('ALHAMBRA HIGH SCHOOL', 'ALHAMBRA HIGH SCHOOL'),
    ('ALISO NIGUEL HIGH SCHOOL', 'ALISO NIGUEL HIGH SCHOOL'),
    ('ARCADIA SENIOR HIGH SCHOOL', 'ARCADIA SENIOR HIGH SCHOOL'),
    ('ARNOLD O BECKMAN HIGH SCHOOL', 'ARNOLD O BECKMAN HIGH SCHOOL'),
    ('ARROYO HIGH SCHOOL', 'ARROYO HIGH SCHOOL'),
    ('BISHOP MONTGOMERY HIGH SCHOOL', 'BISHOP MONTGOMERY HIGH SCHOOL'),
    ('BOLSA GRANDE HIGH SCHOOL', 'BOLSA GRANDE HIGH SCHOOL'),
    ('BREA-OLINDA HIGH SCHOOL', 'BREA-OLINDA HIGH SCHOOL'),
    ('BURBANK SR HIGH SCHOOL', 'BURBANK SR HIGH SCHOOL'),
    ('CALIFORNIA ACADEMY MATH & SCIENCE', 'CALIFORNIA ACADEMY MATH & SCIENCE'),
    ('CANYON HIGH SCHOOL', 'CANYON HIGH SCHOOL'),
    ('CAPISTRANO VALLEY HIGH SCHOOL', 'CAPISTRANO VALLEY HIGH SCHOOL'),
    ('CASTRO VALLEY HIGH SCHOOL', 'CASTRO VALLEY HIGH SCHOOL'),
    ('CENTENNIAL HIGH SCHOOL', 'CENTENNIAL HIGH SCHOOL'),
    ('CERRITOS HIGH SCHOOL', 'CERRITOS HIGH SCHOOL'),
    ('CHINO HILLS HIGH SCHOOL', 'CHINO HILLS HIGH SCHOOL'),
    ('CRESCENTA VALLEY HIGH SCHOOL', 'CRESCENTA VALLEY HIGH SCHOOL'),
    ('CYPRESS HIGH SCHOOL', 'CYPRESS HIGH SCHOOL'),
    ('DIAMOND BAR HIGH SCHOOL', 'DIAMOND BAR HIGH SCHOOL'),
    ('DIAMOND RANCH HIGH SCHOOL', 'DIAMOND RANCH HIGH SCHOOL'),
    ('DOWNEY HIGH SCHOOL', 'DOWNEY HIGH SCHOOL'),
    ('EDISON HIGH SCHOOL', 'EDISON HIGH SCHOOL'),
    ('EL CAMINO REAL SR HIGH SCHOOL', 'EL CAMINO REAL SR HIGH SCHOOL'),
    ('EL TORO HIGH SCHOOL', 'EL TORO HIGH SCHOOL'),
    ('ELEANOR ROOSEVELT HIGH SCHOOL', 'ELEANOR ROOSEVELT HIGH SCHOOL'),
    ('ESPERANZA HIGH SCHOOL', 'ESPERANZA HIGH SCHOOL'),
    ('EVERGREEN VALLEY HIGH SCHOOL', 'EVERGREEN VALLEY HIGH SCHOOL'),
    ('FAIRMONT PREPARATORY ACADEMY', 'FAIRMONT PREPARATORY ACADEMY'),
    ('FOUNTAIN VALLEY HIGH SCHOOL', 'FOUNTAIN VALLEY HIGH SCHOOL'),
    ('FRANCISCO BRAVO MEDICAL MAGNET CENTER', 'FRANCISCO BRAVO MEDICAL MAGNET CENTER'),
    ('GABRIELINO HIGH SCHOOL', 'GABRIELINO HIGH SCHOOL'),
    ('GALILEO HIGH SCHOOL', 'GALILEO HIGH SCHOOL'),
    ('GARDEN GROVE HIGH SCHOOL', 'GARDEN GROVE HIGH SCHOOL'),
    ('GEORGE WASHINGTON HIGH SCHOOL', 'GEORGE WASHINGTON HIGH SCHOOL'),
    ('GLEN A. WILSON HIGH SCHOOL', 'GLEN A. WILSON HIGH SCHOOL'),
    ('GLENDALE SENIOR HIGH SCHOOL', 'GLENDALE SENIOR HIGH SCHOOL'),
    ('GRANADA HILLS HIGH SCHOOL', 'GRANADA HILLS HIGH SCHOOL'),
    ('GRETCHEN WHITNEY HIGH SCHOOL', 'GRETCHEN WHITNEY HIGH SCHOOL'),
    ('GROVER CLEVELAND HIGH SCH. (HUMAN. MAG.)', 'GROVER CLEVELAND HIGH SCH. (HUMAN. MAG.)'),
    ('HECTOR GODINEZ FUNDAMENTAL HS', 'HECTOR GODINEZ FUNDAMENTAL HS'),
    ('HOMESTEAD HIGH SCHOOL', 'HOMESTEAD HIGH SCHOOL'),
    ('HUNTINGTON BEACH HIGH SCHOOL', 'HUNTINGTON BEACH HIGH SCHOOL'),
    ('IRVINE HIGH SCHOOL', 'IRVINE HIGH SCHOOL'),
    ('IRVINGTON HIGH SCHOOL', 'IRVINGTON HIGH SCHOOL'),
    ('JOHN A. ROWLAND HIGH SCHOOL', 'JOHN A. ROWLAND HIGH SCHOOL'),
    ('JOHN F. KENNEDY HIGH SCHOOL', 'JOHN F. KENNEDY HIGH SCHOOL'),
    ('JOHN MARSHALL SR HIGH SCHOOL', 'JOHN MARSHALL SR HIGH SCHOOL'),
    ('LA QUINTA HIGH SCHOOL', 'LA QUINTA HIGH SCHOOL'),
    ('LAKEWOOD SENIOR HIGH SCHOOL', 'LAKEWOOD SENIOR HIGH SCHOOL'),
    ('LOARA HIGH SCHOOL', 'LOARA HIGH SCHOOL'),
    ('LONG BEACH POLYTECHNIC HIGH SCHOOL', 'LONG BEACH POLYTECHNIC HIGH SCHOOL'),
    ('LOS ALAMITOS HIGH SCHOOL', 'LOS ALAMITOS HIGH SCHOOL'),
    ('LOS AMIGOS HIGH SCHOOL', 'LOS AMIGOS HIGH SCHOOL'),
    ('LOS OSOS', 'LOS OSOS'),
    ('LOWELL HIGH SCHOOL', 'LOWELL HIGH SCHOOL'),
    ('LYNBROOK HIGH SCHOOL', 'LYNBROOK HIGH SCHOOL'),
    ('MARINA HIGH SCHOOL', 'MARINA HIGH SCHOOL'),
    ('MARK KEPPEL HIGH SCHOOL', 'MARK KEPPEL HIGH SCHOOL'),
    ('MATER DEI HIGH SCHOOL', 'MATER DEI HIGH SCHOOL'),
    ('MILPITAS HIGH SCHOOL', 'MILPITAS HIGH SCHOOL'),
    ('MISSION SAN JOSE HIGH SCHOOL', 'MISSION SAN JOSE HIGH SCHOOL'),
    ('MONTA VISTA HIGH SCHOOL', 'MONTA VISTA HIGH SCHOOL'),
    ('MONTCLAIR HIGH SCHOOL', 'MONTCLAIR HIGH SCHOOL'),
    ('NORTH HIGH SCHOOL', 'NORTH HIGH SCHOOL'),
    ('NORTHWOOD HIGH SCHOOL', 'NORTHWOOD HIGH SCHOOL'),
    ('ORANGE HIGH SCHOOL', 'ORANGE HIGH SCHOOL'),
    ('OTAY RANCH HIGH SCHOOL', 'OTAY RANCH HIGH SCHOOL'),
    ('OXFORD ACADEMY', 'OXFORD ACADEMY'),
    ('PACIFICA HIGH SCHOOL', 'PACIFICA HIGH SCHOOL'),
    ('PALOS VERDES PENINSULA HIGH SCHOOL', 'PALOS VERDES PENINSULA HIGH SCHOOL'),
    ('PARAMOUNT HIGH SCHOOL', 'PARAMOUNT HIGH SCHOOL'),
    ('PIEDMONT HILLS HIGH SCHOOL', 'PIEDMONT HILLS HIGH SCHOOL'),
    ('RANCHO ALAMITOS HIGH SCHOOL', 'RANCHO ALAMITOS HIGH SCHOOL'),
    ('RANCHO BERNARDO HIGH SCHOOL', 'RANCHO BERNARDO HIGH SCHOOL'),
    ('RANCHO CUCAMONGA HIGH SCHOOL', 'RANCHO CUCAMONGA HIGH SCHOOL'),
    ('RICHARD GAHR HIGH SCHOOL', 'RICHARD GAHR HIGH SCHOOL'),
    ('ROSEMEAD HIGH SCHOOL', 'ROSEMEAD HIGH SCHOOL'),
    ('RUBEN AYALA HIGH SCHOOL', 'RUBEN AYALA HIGH SCHOOL'),
    ('SAN GABRIEL HIGH SCHOOL', 'SAN GABRIEL HIGH SCHOOL'),
    ('SAN MARINO HIGH SCHOOL', 'SAN MARINO HIGH SCHOOL'),
    ('SANTIAGO HIGH SCHOOL', 'SANTIAGO HIGH SCHOOL'),
    ('SANTIAGO HIGH SCHOOL', 'SANTIAGO HIGH SCHOOL'),
    ('SCRIPPS RANCH HIGH SCHOOL', 'SCRIPPS RANCH HIGH SCHOOL'),
    ('SEGERSTROM HIGH SCHOOL', 'SEGERSTROM HIGH SCHOOL'),
    ('SOUTH GATE SR HIGH SCHOOL', 'SOUTH GATE SR HIGH SCHOOL'),
    ('SOUTH HIGH SCHOOL', 'SOUTH HIGH SCHOOL'),
    ('STOCKDALE HIGH SCHOOL', 'STOCKDALE HIGH SCHOOL'),
    ('SUNNY HILLS HIGH SCHOOL', 'SUNNY HILLS HIGH SCHOOL'),
    ('TEMPLE CITY HIGH SCHOOL', 'TEMPLE CITY HIGH SCHOOL'),
    ('TESORO HIGH SCHOOL', 'TESORO HIGH SCHOOL'),
    ('TORRANCE HIGH SCHOOL', 'TORRANCE HIGH SCHOOL'),
    ('TORREY PINES HIGH SCHOOL', 'TORREY PINES HIGH SCHOOL'),
    ('TRABUCO HILLS HIGH SCHOOL', 'TRABUCO HILLS HIGH SCHOOL'),
    ('TROY HIGH SCHOOL', 'TROY HIGH SCHOOL'),
    ('UNIVERSITY HIGH SCHOOL', 'UNIVERSITY HIGH SCHOOL'),
    ('VALENCIA HIGH SCHOOL', 'VALENCIA HIGH SCHOOL'),
    ('VILLA PARK HIGH SCHOOL', 'VILLA PARK HIGH SCHOOL'),
    ('WALNUT HIGH SCHOOL', 'WALNUT HIGH SCHOOL'),
    ('WARREN HIGH SCHOOL', 'WARREN HIGH SCHOOL'),
    ('WEST COVINA HIGH SCHOOL', 'WEST COVINA HIGH SCHOOL'),
    ('WEST HIGH SCHOOL', 'WEST HIGH SCHOOL'),
    ('WESTMINSTER HIGH SCHOOL', 'WESTMINSTER HIGH SCHOOL'),
    ('WESTVIEW', 'WESTVIEW'),
    ('WOODBRIDGE HIGH SCHOOL', 'WOODBRIDGE HIGH SCHOOL'),
    ('WOODROW WILSON HIGH SCHOOL', 'WOODROW WILSON HIGH SCHOOL'),
)

UC_GPA = (
    ('4.00 and above', '4.00 and above'),
    ('3.70-3.99', '3.70-3.99'),
    ('3.30-3.69', '3.30-3.69'),
    ('3.00-3.29', '3.00-3.29'),
    ('Below 3.00', 'Below 3.00')
)

SAT = (
    ('700-800', '700-800'),
    ('600-690', '600-690'),
    ('500-590', '500-590'),
    ('400-490', '400-490'),
    ('Below 400', 'Below 400')
)
class Applicant(models.Model):
    major = models.CharField(max_length = 128, choices = MAJOR)
    gender = models.CharField(max_length = 128, choices = GENDER)
    ethnicity = models.CharField(max_length = 128, choices = ETHNICITY)
    residency = models.CharField(max_length = 128, choices = RESIDENCY)
    high_school = models.CharField(max_length = 128, choices = HIGH_SCHOOL)
    uc_gpa = models.CharField(max_length = 128, choices = UC_GPA)
    sat_verbal = models.CharField(max_length=128, choices=SAT)
    sat_math = models.CharField(max_length = 128, choices = SAT)
    sat_writing = models.CharField(max_length = 128, choices = SAT)

    def get_absolute_url(self):
        return reverse('chancemeuci:index')

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.major, self.gender, self.ethnicity, self.residency, self.high_school)




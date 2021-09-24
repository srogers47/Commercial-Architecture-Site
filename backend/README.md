Get server up and running with standard ./manage.py runserver. 
replacing runserver with tailwind start as docs recommend doesn't currently allow access to django server.


Using django-tailwind:
* Requires node/npm
* I recommend installing node via nvm to avoid breaking dependency issues. 
	See this link: https://github.com/nvm-sh/nvm 


Consistency in preferences. 
Disclaimer: it is not considered best practice to allign to these specific conventions however
 it IS best practice to maintain uniform consistency.  
* All html partial files will begin with an underscore and  live in theme app under partials/   
* All files (html, css, js) will use underscores __ not hyphens or CamelCase
* All css and js files will have lowercase naming convention. (Most css is inline via tailwind)


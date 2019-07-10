# ISTE-NITK_Website

### Things to keep in mind

- Write readable code!
- Use appropriate variable names
- Follow <a href="https://stackoverflow.com/a/1747960/4417613">this</a> convention for storing templates
- Follow template extending whenever possible
- Follow PascalCase only for class names, use '_' to separate words otherwise

### Assumptions

- Sig heads are assigned "staff" status
- Everyone's accounts have to be made manually
- Passwords can be changed once logged in, default username-firstnamelastname, default password-istenitk

### Running instructions
```
  pip3 install requirements.txt
  python3 manage.py runserver 0.0.0.0:8000 #for mobile dev
```

### Contributing

- Place all CSS and JS code in `static/{css or js}/main.{css or js}` (bad practice, code will be refactored later)


To open the website in mobile view you could-

- Use your desktop browser
  - Firefox: https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_Mode
  - Chrome: https://developers.google.com/web/tools/chrome-devtools/device-mode/
  
- Use your mobile browser
  - Ensure your mobile and laptop are on the same network
  - Find your IPv4 address using ipconfig or ifconfig command
  - Use http://IP_address:8000 as the URL to access the website from your mobile browser

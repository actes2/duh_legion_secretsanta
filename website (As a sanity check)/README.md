# This directory is a Sanity Check for the website

What that actually means is that I'm leveraging this location as a localization for our HTML modifications as once we decide to properly implement flask you wont be able to just "live preview" the webpage because bullshit like {{url_for('static'), filename='styles.css'}} will literally be how we call our stylesheet.

Therefore, to maintain consistency, make all web-modifications here, and I will append the results in the 'app' folder.
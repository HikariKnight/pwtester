package main

import (
	"crypto/sha1"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"regexp"
	"strings"
	"time"

	"github.com/therecipe/qt/core"
	"github.com/therecipe/qt/uitools"
	"github.com/therecipe/qt/widgets"
)

func main() {
	// Create our Qt application
	widgets.NewQApplication(len(os.Args), os.Args)
	newMainWindow().Show()
	widgets.QApplication_Exec()
}

func newMainWindow() *widgets.QWidget {

	// Open the .ui file from QML resources (that gets compiled into the binary)
	file := core.NewQFile2(":/qml/main.ui")
	file.Open(core.QIODevice__ReadOnly)

	// Load the UI
	formWidget := uitools.NewQUiLoader(nil).Load(file, nil)
	file.Close()

	// Define our static widgets from the UI file
	var (
		aboutButton  = widgets.NewQPushButtonFromPointer(formWidget.FindChild("aboutButton", core.Qt__FindChildrenRecursively).Pointer())
		okButton     = widgets.NewQPushButtonFromPointer(formWidget.FindChild("okButton", core.Qt__FindChildrenRecursively).Pointer())
		passwordEdit = widgets.NewQLineEditFromPointer(formWidget.FindChild("passwordEdit", core.Qt__FindChildrenRecursively).Pointer())
		resultLbl    = widgets.NewQLabelFromPointer(formWidget.FindChild("resultLbl", core.Qt__FindChildrenRecursively).Pointer())
	)

	passwordEdit.SetFocus(core.Qt__OtherFocusReason)

	// When the about button is clicked, provide some about info and display it in a messagebox
	aboutButton.ConnectClicked(func(flag bool) {
		var aboutText string = "A small open source program written in GO by HikariKnight\n" +
			"to check if a password has been in any known breaches\n" +
			"reported to haveibeenpwned.com\n\n" +
			"The password typed in is hashed and not exposed to haveibeenpwned!\n" +
			"Only the first 5 characters of the\n" +
			"hashed password is exposed to the API,\n" +
			"the program then checks the list from HIBP\n" +
			"to see if the remainder of the hash is in the database."

		// Display an information messagebox with the text
		widgets.QMessageBox_Information(
			nil,
			"Password Tester",
			aboutText,
			widgets.QMessageBox__Ok,
			widgets.QMessageBox__Ok,
		)
	})

	checkPassword := func() {
		// Hash the password in the LineEdit
		hash := sha1.New()
		io.WriteString(hash, passwordEdit.Text())

		// Cast the byte slice to an uppercase string so we can use it
		pwHash := strings.ToUpper(
			fmt.Sprintf(
				"%x", hash.Sum(nil),
			),
		)

		// Create a http client with a 30 second timeout
		client := &http.Client{
			Timeout: 30 * time.Second,
		}

		// Define our request where we only send the first 5 characters of the hash
		request, err := http.NewRequest("GET", "https://api.pwnedpasswords.com/range/"+pwHash[:5], nil)
		if err != nil {
			log.Fatal(err)
		}
		// Set the user agent header
		request.Header.Set("User-Agent", "Mozilla")

		// Make request
		response, err := client.Do(request)
		if err != nil {
			log.Fatal(err)
		}
		// Close the response body at the end of the function
		defer response.Body.Close()

		// Read the response body
		contentBytes, err := ioutil.ReadAll(response.Body)
		// Convert to string
		contentString := string(contentBytes)

		// Make a regex for our search for the remainder of our hash
		testBreach, _ := regexp.Compile(pwHash[5:] + `:\d+`)

		// Get the result from our search
		result := testBreach.FindString(contentString)
		if result == "" {
			// Password is not found in the breached password hash list
			// Change the result label to green with the result
			resultLbl.SetText(
				`<html><head/><body><p>Result:<br/><span style=" color:#08a700;">
				Password not found in any known breaches.</span></p></body></html>`,
			)
		} else {
			// Password is found in the breached password hash list
			// Split the result string by :
			breachCount := strings.Split(result, ":")

			/* Change the result label to red with a message showing it is an insecure password
			   and also show how many times the password has been in a breach */
			resultLbl.SetText(
				fmt.Sprintf(
					`<html><head/><body><p>Result:<br/><span style=" color:#ff0004;">
					Password has appeared in one or more data breaches!<br/>
					It has been sighted %s times</span></p></body></html>`,
					breachCount[1],
				),
			)

			// Display a messagebox that tells the user HEY! Your password is not secure!
			widgets.QMessageBox_Warning(
				nil,
				"PASSWORD BREACHED!",
				"The password you have entered has been found in a known breach!\n"+
					"Avoid using the password you just tested at all cost!",
				widgets.QMessageBox__Ok,
				widgets.QMessageBox__Ok,
			)
		}
	}

	// Connect ok button and passwordedit to the checkPassword function
	okButton.ConnectClicked(func(flag bool) {
		checkPassword()
	})

	passwordEdit.ConnectReturnPressed(func() {
		checkPassword()
	})

	// Return the finished UI
	return formWidget
}

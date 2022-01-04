package day_6;

import java.util.Arrays;
import java.util.List;

public class RegistrationService{
	public void validateEmail(String email) {
		if (!isDomainValid(email)) {
			throw new DomainNotValidateException ("Invalid Domain");
		}
	}
	private boolean isDomainValid (String email) {
		List<String> validDomains = Arrays.asList("gmail.com" , "yahoo.com","outlook.com");
		if (validDomains.contains(email.substring(email.indexOf("@")+1))) {
			return true;
		}
		return false;
	}
	
}

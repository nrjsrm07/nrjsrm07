package day_6;


public class ServiceClient{
	public static void main(String[] args) {
		RegistrationService service = new RegistrationService();
		service.validateEmail("Abc@google.com");
		service.validateEmail("Abc@gmail.com");
	}
}
​​​​​